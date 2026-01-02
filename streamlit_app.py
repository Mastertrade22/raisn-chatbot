"""
Streamlit Web Interface for Real Estate Chatbot
Uses the modular chatbot_core for easy maintenance and deployment
"""

import streamlit as st
from typing import List
import os

from chatbot_core import create_chatbot
from config import AVAILABLE_MODELS, AVAILABLE_CLIENTS, DEFAULT_CLIENT, validate_config
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
    .glm-badge {
        background-color: #10b981;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbots" not in st.session_state:
    st.session_state.chatbots = {}

if "selected_client" not in st.session_state:
    st.session_state.selected_client = DEFAULT_CLIENT


def initialize_chatbots():
    """Initialize chatbot instances for all available models"""
    try:
        # Get current tenant_id
        tenant_id = AVAILABLE_CLIENTS.get(st.session_state.selected_client, {}).get("id")

        # Initialize all available models
        for model_key, model_config in AVAILABLE_MODELS.items():
            if model_key not in st.session_state.chatbots:
                st.session_state.chatbots[model_key] = create_chatbot(
                    model_id=model_config["id"],
                    tenant_id=tenant_id
                )
    except Exception as e:
        st.error(f"Failed to initialize chatbots: {str(e)}")


# Sidebar
with st.sidebar:
    st.title("🏠 Real Estate Chatbot")
    st.markdown("---")

    # Model selection
    st.subheader("⚙️ Settings")

    # Create model options from AVAILABLE_MODELS
    model_display_to_key = {config["display_name"]: key for key, config in AVAILABLE_MODELS.items()}
    model_options = list(model_display_to_key.keys())

    selected_models = st.multiselect(
        "Choose AI Model(s):",
        model_options,
        default=[model_options[0]] if model_options else [],
        help="Select one or more AI models to compare responses"
    )

    st.markdown("---")

    # Client selection
    st.subheader("🏢 Client Filter")

    client_options = {key: config["display_name"] for key, config in AVAILABLE_CLIENTS.items()}
    selected_client_key = st.selectbox(
        "Select Client:",
        options=list(client_options.keys()),
        format_func=lambda x: client_options[x],
        index=list(client_options.keys()).index(st.session_state.selected_client),
        help="Filter projects by client/developer (POC mode - in production, this comes from backend)"
    )

    # Show client description
    if selected_client_key in AVAILABLE_CLIENTS:
        st.caption(AVAILABLE_CLIENTS[selected_client_key]["description"])

    # Update chatbot tenant if changed
    if selected_client_key != st.session_state.selected_client:
        st.session_state.selected_client = selected_client_key
        tenant_id = AVAILABLE_CLIENTS[selected_client_key]["id"]

        # Update all chatbots
        for chatbot in st.session_state.chatbots.values():
            if chatbot:
                chatbot.set_tenant(tenant_id)

        st.info(f"🔄 Client filter updated to: {AVAILABLE_CLIENTS[selected_client_key]['display_name']}")

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
        for chatbot in st.session_state.chatbots.values():
            if chatbot:
                chatbot.reset_history()
        st.rerun()

    st.markdown("---")
    st.caption("Built with LangGraph & Streamlit")

# Main chat interface
st.title("💬 Chat with Real Estate AI")
st.markdown("Ask questions about real estate projects, pricing, availability, and more!")

# Initialize chatbots
initialize_chatbots()

# Helper function to get model color
def get_model_color(model_name):
    """Get badge color based on model name"""
    model_lower = model_name.lower()
    if "qwen" in model_lower:
        return "qwen-badge"
    elif "deepseek" in model_lower:
        return "deepseek-badge"
    elif "glm" in model_lower:
        return "glm-badge"
    else:
        return "qwen-badge"  # Default color

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "model" in message:
            # Display model badge for assistant messages
            model_color = get_model_color(message.get("model_display", ""))
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
    if not selected_models:
        st.warning("⚠️ Please select at least one model to continue")
    else:
        # Process each selected model
        for model_display in selected_models:
            model_key = model_display_to_key.get(model_display)
            if not model_key or model_key not in st.session_state.chatbots:
                st.error(f"Model {model_display} not initialized")
                continue

            chatbot = st.session_state.chatbots[model_key]

            with st.chat_message("assistant"):
                model_color = get_model_color(model_display)
                st.markdown(f'<div class="model-badge {model_color}">{model_display}</div>', unsafe_allow_html=True)

                with st.spinner(f"Thinking with {model_display}..."):
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
                        error_msg = f"Error with {model_display}: {str(e)}"
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
