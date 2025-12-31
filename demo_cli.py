"""
CLI Demo Script
Simple command-line interface to test the chatbot core functionality
This demonstrates how easy it is to plug the chatbot into any application
"""

from chatbot_core import create_chatbot
from config import AVAILABLE_MODELS, validate_config
from database import db_interface


def print_banner():
    """Print welcome banner"""
    print("\n" + "="*70)
    print("🏠 Real Estate AI Chatbot - CLI Demo")
    print("="*70)
    print("\nThis demo shows how the core chatbot can be used in any application.")
    print("Type 'quit' or 'exit' to stop, 'clear' to reset history.\n")


def print_response(response: dict, show_details: bool = True):
    """
    Print chatbot response

    Args:
        response: Response dict from chatbot
        show_details: Whether to show SQL query and other details
    """
    print(f"\n🤖 Assistant: {response['final_answer']}\n")

    if show_details and response['query_type'] == 'data' and response['sql_query']:
        print(f"📊 Query Type: {response['query_type']}")
        print(f"🔍 SQL Query: {response['sql_query']}\n")

    if response.get('error'):
        print(f"⚠️  Warning: {response['error']}\n")


def select_model():
    """
    Let user select a model

    Returns:
        str: Model ID
    """
    print("\n🤖 Available Models:")
    for idx, (key, model_info) in enumerate(AVAILABLE_MODELS.items(), 1):
        print(f"  {idx}. {model_info['display_name']}")

    while True:
        choice = input(f"\nSelect model (1-{len(AVAILABLE_MODELS)}) [default: 1]: ").strip()
        if not choice:
            choice = "1"

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(AVAILABLE_MODELS):
                model_key = list(AVAILABLE_MODELS.keys())[idx]
                return AVAILABLE_MODELS[model_key]['id']
            else:
                print(f"Please enter a number between 1 and {len(AVAILABLE_MODELS)}")
        except ValueError:
            print("Please enter a valid number")


def run_interactive_demo():
    """Run interactive CLI demo"""
    try:
        # Validate configuration
        validate_config()

        print_banner()

        # Check database
        print("📁 Checking database...")
        if db_interface.test_connection():
            counts = db_interface.get_table_counts()
            print(f"✅ Database connected: {counts.get('projects', 0)} projects, {counts.get('project_units', 0)} units\n")
        else:
            print("⚠️  Database connection issue. Chatbot may not work correctly.\n")

        # Select model
        model_id = select_model()
        print(f"\n✅ Using model: {model_id}")

        # Create chatbot
        print("\n🔧 Initializing chatbot...")
        chatbot = create_chatbot(model_id=model_id)
        print("✅ Chatbot ready!\n")

        # Main loop
        while True:
            try:
                # Get user input
                question = input("👤 You: ").strip()

                if not question:
                    continue

                # Check for commands
                if question.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Goodbye!\n")
                    break

                if question.lower() == 'clear':
                    chatbot.reset_history()
                    print("\n🗑️  Chat history cleared!\n")
                    continue

                if question.lower() == 'history':
                    history = chatbot.get_history()
                    print("\n📜 Chat History:")
                    for msg in history:
                        role = "You" if msg['role'] == 'user' else "Assistant"
                        print(f"  {role}: {msg['content'][:100]}...")
                    print()
                    continue

                # Get response from chatbot
                print("\n🤔 Thinking...")
                response = chatbot.ask(question)

                # Print response
                print_response(response)

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break

            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")

    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}\n")
        print("Please check your configuration and try again.\n")


def run_batch_demo():
    """Run batch demo with predefined questions"""
    try:
        validate_config()

        print_banner()
        print("📋 Running batch demo with sample questions...\n")

        # Create chatbot
        model_id = AVAILABLE_MODELS["qwen"]["id"]
        chatbot = create_chatbot(model_id=model_id)

        # Sample questions
        questions = [
            "Hello!",
            "How many projects are under construction?",
            "Show me all 3BHK units",
            "What is the average price per sqft?",
        ]

        for question in questions:
            print(f"👤 You: {question}")
            response = chatbot.ask(question)
            print_response(response, show_details=False)
            print("-" * 70)

        print("\n✅ Batch demo completed!\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--batch":
        run_batch_demo()
    else:
        run_interactive_demo()
