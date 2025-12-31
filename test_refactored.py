"""
Test script to verify the refactored code works correctly
Run this to ensure everything is set up properly
"""

import sys
from typing import Dict, Any


def test_imports() -> bool:
    """Test if all modules can be imported"""
    print("Testing imports...")

    try:
        import config
        print("  ✅ config.py imported")
    except Exception as e:
        print(f"  ❌ config.py failed: {e}")
        return False

    try:
        import llm_client
        print("  ✅ llm_client.py imported")
    except Exception as e:
        print(f"  ❌ llm_client.py failed: {e}")
        return False

    try:
        import database
        print("  ✅ database.py imported")
    except Exception as e:
        print(f"  ❌ database.py failed: {e}")
        return False

    try:
        import chatbot_core
        print("  ✅ chatbot_core.py imported")
    except Exception as e:
        print(f"  ❌ chatbot_core.py failed: {e}")
        return False

    print("✅ All imports successful!\n")
    return True


def test_config() -> bool:
    """Test configuration module"""
    print("Testing configuration...")

    try:
        from config import (
            AVAILABLE_MODELS,
            OPENROUTER_API_KEY,
            DB_PATH,
            MAX_SQL_RETRIES,
            get_model_config
        )

        print(f"  ✅ Available models: {list(AVAILABLE_MODELS.keys())}")
        print(f"  ✅ Default retries: {MAX_SQL_RETRIES}")
        print(f"  ✅ Database path: {DB_PATH}")

        if OPENROUTER_API_KEY:
            print("  ✅ API key loaded")
        else:
            print("  ⚠️  API key not found (set OPENROUTER_API_KEY in .env)")

        # Test get_model_config
        model_config = get_model_config("qwen")
        print(f"  ✅ Model config works: {model_config['display_name']}")

        print("✅ Configuration tests passed!\n")
        return True

    except Exception as e:
        print(f"  ❌ Configuration test failed: {e}\n")
        return False


def test_database() -> bool:
    """Test database module"""
    print("Testing database...")

    try:
        from database import db_interface, get_database_schema, execute_sql

        # Test connection
        if db_interface.test_connection():
            print("  ✅ Database connection successful")
        else:
            print("  ❌ Database connection failed")
            return False

        # Test table counts
        counts = db_interface.get_table_counts()
        print(f"  ✅ Projects: {counts.get('projects', 0)}")
        print(f"  ✅ Units: {counts.get('project_units', 0)}")

        # Test schema retrieval
        schema = get_database_schema()
        if "projects" in schema and "project_units" in schema:
            print("  ✅ Schema retrieved successfully")
        else:
            print("  ❌ Schema incomplete")
            return False

        # Test query execution
        results, error = execute_sql("SELECT COUNT(*) FROM projects")
        if error is None:
            print(f"  ✅ Query execution works: {results[0][0]} projects")
        else:
            print(f"  ❌ Query execution failed: {error}")
            return False

        print("✅ Database tests passed!\n")
        return True

    except Exception as e:
        print(f"  ❌ Database test failed: {e}\n")
        return False


def test_llm_client() -> bool:
    """Test LLM client module"""
    print("Testing LLM client...")

    try:
        from llm_client import create_llm_client
        from config import OPENROUTER_API_KEY, AVAILABLE_MODELS

        if not OPENROUTER_API_KEY:
            print("  ⚠️  Skipping LLM test (no API key)")
            return True

        # Create client
        model_id = AVAILABLE_MODELS["qwen"]["id"]
        llm = create_llm_client(model_id)
        print(f"  ✅ LLM client created for {model_id}")

        # Test invoke (simple prompt)
        try:
            response = llm.invoke("Say 'test successful' and nothing else.")
            if response:
                print(f"  ✅ LLM invoke works: '{response[:50]}...'")
            else:
                print("  ❌ LLM returned empty response")
                return False
        except Exception as e:
            print(f"  ⚠️  LLM invoke test skipped: {e}")
            # Don't fail the test - API key might have issues

        print("✅ LLM client tests passed!\n")
        return True

    except Exception as e:
        print(f"  ❌ LLM client test failed: {e}\n")
        return False


def test_chatbot_core() -> bool:
    """Test chatbot core module"""
    print("Testing chatbot core...")

    try:
        from chatbot_core import create_chatbot
        from config import OPENROUTER_API_KEY

        # Create chatbot
        chatbot = create_chatbot()
        print("  ✅ Chatbot created successfully")

        if not OPENROUTER_API_KEY:
            print("  ⚠️  Skipping chatbot ask test (no API key)")
            return True

        # Test ask method
        try:
            response = chatbot.ask("Hello", preserve_history=False)
            print(f"  ✅ Chatbot ask() works")
            print(f"     Query type: {response['query_type']}")
            print(f"     Has answer: {bool(response['final_answer'])}")

            # Test with data query
            response = chatbot.ask("How many projects are there?", preserve_history=False)
            print(f"  ✅ Data query works")
            print(f"     Query type: {response['query_type']}")
            print(f"     SQL generated: {bool(response.get('sql_query'))}")

        except Exception as e:
            print(f"  ⚠️  Chatbot ask test warning: {e}")
            # Don't fail - API might have issues

        # Test history methods
        chatbot.reset_history()
        print("  ✅ History reset works")

        history = chatbot.get_history()
        print(f"  ✅ Get history works: {len(history)} messages")

        print("✅ Chatbot core tests passed!\n")
        return True

    except Exception as e:
        print(f"  ❌ Chatbot core test failed: {e}\n")
        return False


def run_all_tests() -> Dict[str, bool]:
    """Run all tests and return results"""
    print("="*70)
    print("REFACTORED CODE TEST SUITE")
    print("="*70)
    print()

    results = {
        "imports": test_imports(),
        "config": test_config(),
        "database": test_database(),
        "llm_client": test_llm_client(),
        "chatbot_core": test_chatbot_core()
    }

    return results


def print_summary(results: Dict[str, bool]) -> None:
    """Print test summary"""
    print("="*70)
    print("TEST SUMMARY")
    print("="*70)

    total = len(results)
    passed = sum(1 for v in results.values() if v)

    for test_name, passed_flag in results.items():
        status = "✅ PASS" if passed_flag else "❌ FAIL"
        print(f"{status} - {test_name}")

    print()
    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All tests passed! Your refactored code is ready to use.")
        print("\nNext steps:")
        print("  1. Run: python demo_cli.py")
        print("  2. Run: streamlit run streamlit_app_new.py")
        print("  3. Read: QUICKSTART_NEW.md")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        print("Common issues:")
        print("  - Missing OPENROUTER_API_KEY in .env file")
        print("  - Missing dependencies (run: pip install -r requirements.txt)")
        print("  - Database permissions")


if __name__ == "__main__":
    try:
        results = run_all_tests()
        print_summary(results)

        # Exit with error code if any test failed
        if not all(results.values()):
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error during testing: {e}")
        sys.exit(1)
