"""
Streamlit Web Interface for LangGraph Real Estate Chatbot
"""

import streamlit as st
from typing import List
import os
from dotenv import load_dotenv
from app import create_graph, get_database_schema

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Real Estate AI Chatbot",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better chat UI
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .model-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .qwen-badge {
        background-color: #3b82f6;
        color: white;
    }
    .deepseek-badge {
        background-color: #8b5cf6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.title("🏠 Real Estate Chatbot")
    st.markdown("---")

    # Model selection
    st.subheader("⚙️ Settings")

    selected_model = st.radio(
        "Choose AI Model:",
        ["Qwen 2.5 (72B)", "DeepSeek V3", "Both (Comparison)"],
        help="Select which AI model to use for responses"
    )

    # Map display names to model IDs
    model_mapping = {
        "Qwen 2.5 (72B)": "qwen/qwen-2.5-72b-instruct",
        "DeepSeek V3": "deepseek/deepseek-chat"
    }

    st.markdown("---")

    # API Key status
    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key:
        st.success("✅ API Key Loaded")
    else:
        st.error("❌ No API Key Found")
        st.info("Add OPENROUTER_API_KEY to your .env file or Streamlit secrets")

    st.markdown("---")

    # Example questions
    st.subheader("💡 Try asking:")
    example_questions = [
        "How many projects are under construction?",
        "Show me all 3BHK units",
        "What is the cheapest 2BHK?",
        "Which projects have festive offers?",
        "Projects near the airport",
        "Average price per sqft for villas"
    ]

    for question in example_questions:
        if st.button(question, key=f"example_{question}", use_container_width=True):
            st.session_state.user_input = question

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")
    st.caption("Built with LangGraph & Streamlit")

# Main chat interface
st.title("💬 Chat with Real Estate AI")
st.markdown("Ask questions about real estate projects, pricing, availability, and more!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "model" in message:
            # Display model badge for assistant messages
            model_color = "qwen-badge" if "qwen" in message["model"].lower() else "deepseek-badge"
            st.markdown(f'<div class="model-badge {model_color}">{message["model_display"]}</div>', unsafe_allow_html=True)
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about real estate projects..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process with selected model(s)
    if selected_model == "Both (Comparison)":
        # Compare both models
        for model_name, model_id in model_mapping.items():
            with st.chat_message("assistant"):
                model_display = model_name
                model_color = "qwen-badge" if "qwen" in model_id.lower() else "deepseek-badge"
                st.markdown(f'<div class="model-badge {model_color}">{model_display}</div>', unsafe_allow_html=True)

                with st.spinner(f"Thinking with {model_name}..."):
                    try:
                        # Create graph for this model
                        graph = create_graph(model_id)

                        # Initial state
                        initial_state = {
                            "question": prompt,
                            "chat_history": st.session_state.chat_history,
                            "query_type": "",
                            "sql_query": "",
                            "sql_result": "",
                            "final_answer": "",
                            "error": "",
                            "retry_count": 0,
                            "model_name": model_id
                        }

                        # Run the graph
                        final_state = graph.invoke(initial_state)
                        response = final_state['final_answer']

                        # Display response
                        st.markdown(response)

                        # Show SQL query if it was a data query
                        if final_state['query_type'] == 'data' and final_state.get('sql_query'):
                            with st.expander("🔍 View SQL Query"):
                                st.code(final_state['sql_query'], language="sql")

                        # Store in session
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response,
                            "model": model_id,
                            "model_display": model_display
                        })

                    except Exception as e:
                        error_msg = f"Error with {model_name}: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg,
                            "model": model_id,
                            "model_display": model_display
                        })
    else:
        # Single model response
        model_id = model_mapping[selected_model]
        model_display = selected_model

        with st.chat_message("assistant"):
            model_color = "qwen-badge" if "qwen" in model_id.lower() else "deepseek-badge"
            st.markdown(f'<div class="model-badge {model_color}">{model_display}</div>', unsafe_allow_html=True)

            with st.spinner(f"Thinking with {selected_model}..."):
                try:
                    # Create graph for this model
                    graph = create_graph(model_id)

                    # Initial state
                    initial_state = {
                        "question": prompt,
                        "chat_history": st.session_state.chat_history,
                        "query_type": "",
                        "sql_query": "",
                        "sql_result": "",
                        "final_answer": "",
                        "error": "",
                        "retry_count": 0,
                        "model_name": model_id
                    }

                    # Run the graph
                    final_state = graph.invoke(initial_state)
                    response = final_state['final_answer']

                    # Display response
                    st.markdown(response)

                    # Show SQL query if it was a data query
                    if final_state['query_type'] == 'data' and final_state.get('sql_query'):
                        with st.expander("🔍 View SQL Query"):
                            st.code(final_state['sql_query'], language="sql")

                    # Store in session
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "model": model_id,
                        "model_display": model_display
                    })

                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg,
                        "model": model_id,
                        "model_display": model_display
                    })

    # Update chat history for context
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    # Keep only last 5 messages for context
    st.session_state.chat_history = st.session_state.chat_history[-5:]

# Footer
st.markdown("---")
st.caption("This chatbot uses LangGraph with OpenRouter API to query a real estate database.")
