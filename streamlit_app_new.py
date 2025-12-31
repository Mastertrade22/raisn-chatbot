"""
Streamlit Web Interface for Real Estate Chatbot
Uses the modular chatbot_core for easy maintenance and deployment
"""

import streamlit as st
from typing import List
import os

from chatbot_core import create_chatbot
from config import AVAILABLE_MODELS, validate_config
from database import db_interface

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

if "chatbot_qwen" not in st.session_state:
    st.session_state.chatbot_qwen = None

if "chatbot_deepseek" not in st.session_state:
    st.session_state.chatbot_deepseek = None


def initialize_chatbots():
    """Initialize chatbot instances"""
    try:
        if st.session_state.chatbot_qwen is None:
            st.session_state.chatbot_qwen = create_chatbot(
                model_id=AVAILABLE_MODELS["qwen"]["id"]
            )

        if st.session_state.chatbot_deepseek is None:
            st.session_state.chatbot_deepseek = create_chatbot(
                model_id=AVAILABLE_MODELS["deepseek"]["id"]
            )
    except Exception as e:
        st.error(f"Failed to initialize chatbots: {str(e)}")


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

    st.markdown("---")

    # Database status
    try:
        if db_interface.test_connection():
            counts = db_interface.get_table_counts()
            st.success("✅ Database Connected")
            st.info(f"📊 {counts.get('projects', 0)} projects, {counts.get('project_units', 0)} units")
        else:
            st.error("❌ Database Connection Issue")
    except Exception as e:
        st.error(f"❌ Database Error: {str(e)}")

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
        if st.session_state.chatbot_qwen:
            st.session_state.chatbot_qwen.reset_history()
        if st.session_state.chatbot_deepseek:
            st.session_state.chatbot_deepseek.reset_history()
        st.rerun()

    st.markdown("---")
    st.caption("Built with LangGraph & Streamlit")

# Main chat interface
st.title("💬 Chat with Real Estate AI")
st.markdown("Ask questions about real estate projects, pricing, availability, and more!")

# Initialize chatbots
initialize_chatbots()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "model" in message:
            # Display model badge for assistant messages
            model_color = "qwen-badge" if "qwen" in message["model"].lower() else "deepseek-badge"
            st.markdown(f'<div class="model-badge {model_color}">{message["model_display"]}</div>', unsafe_allow_html=True)
        st.markdown(message["content"])

        # Show SQL query if available
        if message["role"] == "assistant" and message.get("sql_query"):
            with st.expander("🔍 View SQL Query"):
                st.code(message["sql_query"], language="sql")

# Chat input
if prompt := st.chat_input("Ask about real estate projects..."):
    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process with selected model(s)
    if selected_model == "Both (Comparison)":
        # Compare both models
        chatbots = {
            "Qwen 2.5 (72B)": st.session_state.chatbot_qwen,
            "DeepSeek V3": st.session_state.chatbot_deepseek
        }

        for model_name, chatbot in chatbots.items():
            with st.chat_message("assistant"):
                model_color = "qwen-badge" if "qwen" in model_name.lower() else "deepseek-badge"
                st.markdown(f'<div class="model-badge {model_color}">{model_name}</div>', unsafe_allow_html=True)

                with st.spinner(f"Thinking with {model_name}..."):
                    try:
                        # Get response from chatbot
                        response = chatbot.ask(prompt)

                        # Display response
                        st.markdown(response['final_answer'])

                        # Show SQL query if it was a data query
                        if response['query_type'] == 'data' and response.get('sql_query'):
                            with st.expander("🔍 View SQL Query"):
                                st.code(response['sql_query'], language="sql")

                        # Store in session
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response['final_answer'],
                            "model": chatbot.model_id,
                            "model_display": model_name,
                            "sql_query": response.get('sql_query', '')
                        })

                    except Exception as e:
                        error_msg = f"Error with {model_name}: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg,
                            "model": chatbot.model_id,
                            "model_display": model_name,
                            "sql_query": ''
                        })
    else:
        # Single model response
        chatbot = st.session_state.chatbot_qwen if "Qwen" in selected_model else st.session_state.chatbot_deepseek
        model_display = selected_model

        with st.chat_message("assistant"):
            model_color = "qwen-badge" if "qwen" in selected_model.lower() else "deepseek-badge"
            st.markdown(f'<div class="model-badge {model_color}">{model_display}</div>', unsafe_allow_html=True)

            with st.spinner(f"Thinking with {selected_model}..."):
                try:
                    # Get response from chatbot
                    response = chatbot.ask(prompt)

                    # Display response
                    st.markdown(response['final_answer'])

                    # Show SQL query if it was a data query
                    if response['query_type'] == 'data' and response.get('sql_query'):
                        with st.expander("🔍 View SQL Query"):
                            st.code(response['sql_query'], language="sql")

                    # Store in session
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response['final_answer'],
                        "model": chatbot.model_id,
                        "model_display": model_display,
                        "sql_query": response.get('sql_query', '')
                    })

                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg,
                        "model": chatbot.model_id,
                        "model_display": model_display,
                        "sql_query": ''
                    })

# Footer
st.markdown("---")
st.caption("This chatbot uses the modular chatbot_core for easy deployment to production.")
