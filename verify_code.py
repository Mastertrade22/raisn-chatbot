"""
Comprehensive code verification script
Checks syntax, imports, database, and code logic without running the full app
"""

import sys
import sqlite3
import json

def check_syntax():
    """Check Python syntax for all files"""
    print("="*70)
    print("1. SYNTAX CHECK")
    print("="*70 + "\n")

    files_to_check = ['app.py', 'real_estate_db.py', 'test_db.py']

    for filename in files_to_check:
        try:
            with open(filename, 'r') as f:
                compile(f.read(), filename, 'exec')
            print(f"✓ {filename}: Syntax OK")
        except SyntaxError as e:
            print(f"✗ {filename}: Syntax Error - {e}")
            return False

    print()
    return True


def check_imports():
    """Check required imports (excluding langgraph)"""
    print("="*70)
    print("2. IMPORT CHECK")
    print("="*70 + "\n")

    required_imports = {
        'typing': ['TypedDict', 'List', 'Literal'],
        'os': [],
        'sqlite3': [],
        'json': [],
        'requests': [],
        'dotenv': ['load_dotenv']
    }

    all_ok = True

    for module, items in required_imports.items():
        try:
            if items:
                exec(f"from {module} import {', '.join(items)}")
            else:
                exec(f"import {module}")
            print(f"✓ {module}: Available")
        except ImportError as e:
            print(f"✗ {module}: MISSING - {e}")
            all_ok = False

    # Check langgraph separately (optional for verification)
    try:
        from langgraph.graph import StateGraph, END
        print(f"✓ langgraph: Available")
    except ImportError:
        print(f"⚠ langgraph: NOT INSTALLED (required to run app.py)")
        print(f"  Install with: pip install -r requirements.txt")

    print()
    return all_ok


def check_database():
    """Verify database structure and data"""
    print("="*70)
    print("3. DATABASE CHECK")
    print("="*70 + "\n")

    try:
        # Import and create database
        from real_estate_db import create_real_estate_db
        schema = create_real_estate_db()

        # Connect and verify
        conn = sqlite3.connect("real_estate_data.db")
        cursor = conn.cursor()

        # Check tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]

        expected_tables = ['projects', 'project_units']
        for table in expected_tables:
            if table in tables:
                print(f"✓ Table '{table}': EXISTS")
            else:
                print(f"✗ Table '{table}': MISSING")
                return False

        # Check data counts
        cursor.execute("SELECT COUNT(*) FROM projects")
        project_count = cursor.fetchone()[0]
        print(f"✓ Projects: {project_count} records")

        cursor.execute("SELECT COUNT(*) FROM project_units")
        unit_count = cursor.fetchone()[0]
        print(f"✓ Units: {unit_count} records")

        # Check indexes
        cursor.execute("SELECT name FROM sqlite_master WHERE type='index'")
        indexes = [row[0] for row in cursor.fetchall()]
        print(f"✓ Indexes: {len(indexes)} created")

        conn.close()
        print()
        return True

    except Exception as e:
        print(f"✗ Database Error: {e}")
        print()
        return False


def check_code_logic():
    """Verify code logic and structure"""
    print("="*70)
    print("4. CODE LOGIC CHECK")
    print("="*70 + "\n")

    try:
        # Import main modules
        from real_estate_db import create_real_estate_db

        # Check app.py structure (without running)
        with open('app.py', 'r') as f:
            app_code = f.read()

        # Check for key components
        checks = {
            'AgentState TypedDict': 'class AgentState(TypedDict):' in app_code,
            'Router System Prompt': 'ROUTER_SYSTEM_PROMPT' in app_code,
            'SQL Generator Prompt': 'SQL_GENERATOR_SYSTEM_PROMPT' in app_code,
            'Response Prompt': 'RESPONSE_SYSTEM_PROMPT' in app_code,
            'OpenRouterLLM class': 'class OpenRouterLLM:' in app_code,
            'router_node function': 'def router_node(state: AgentState)' in app_code,
            'sql_gen_node function': 'def sql_gen_node(state: AgentState)' in app_code,
            'execute_sql_node function': 'def execute_sql_node(state: AgentState)' in app_code,
            'response_node function': 'def response_node(state: AgentState)' in app_code,
            'Error handling in API': 'except requests.exceptions.Timeout:' in app_code,
            'Error handling in nodes': 'except Exception as e:' in app_code,
            'Model comparison': 'def compare_models(' in app_code,
            'User-friendly errors': 'I apologize, but' in app_code,
        }

        all_ok = True
        for name, exists in checks.items():
            if exists:
                print(f"✓ {name}")
            else:
                print(f"✗ {name}: MISSING")
                all_ok = False

        print()
        return all_ok

    except Exception as e:
        print(f"✗ Code Logic Error: {e}")
        print()
        return False


def check_test_queries():
    """Test sample SQL queries"""
    print("="*70)
    print("5. SAMPLE QUERIES TEST")
    print("="*70 + "\n")

    try:
        conn = sqlite3.connect("real_estate_data.db")
        cursor = conn.cursor()

        queries = [
            ("Count projects", "SELECT COUNT(*) FROM projects"),
            ("Count units", "SELECT COUNT(*) FROM project_units"),
            ("Projects under construction",
             "SELECT COUNT(*) FROM projects WHERE construction_status = 'Under Construction'"),
            ("Cheapest 2BHK",
             "SELECT project_name FROM projects p JOIN project_units u ON p.project_id = u.project_id WHERE u.configuration_type = '2BHK' ORDER BY u.base_price ASC LIMIT 1"),
            ("Units with offers",
             "SELECT COUNT(*) FROM project_units WHERE current_festive_offers IS NOT NULL"),
        ]

        all_ok = True
        for name, query in queries:
            try:
                cursor.execute(query)
                result = cursor.fetchone()
                print(f"✓ {name}: {result[0] if result else 'OK'}")
            except Exception as e:
                print(f"✗ {name}: {e}")
                all_ok = False

        conn.close()
        print()
        return all_ok

    except Exception as e:
        print(f"✗ Query Test Error: {e}")
        print()
        return False


def check_documentation():
    """Check documentation files"""
    print("="*70)
    print("6. DOCUMENTATION CHECK")
    print("="*70 + "\n")

    docs = [
        'README.md',
        'DATABASE_SCHEMA.md',
        'SYSTEM_PROMPTS.md',
        'QUICKSTART.md',
        'requirements.txt',
        '.env.example'
    ]

    all_ok = True
    for doc in docs:
        try:
            with open(doc, 'r') as f:
                content = f.read()
                if len(content) > 0:
                    print(f"✓ {doc}: {len(content)} bytes")
                else:
                    print(f"⚠ {doc}: Empty file")
        except FileNotFoundError:
            print(f"✗ {doc}: MISSING")
            all_ok = False

    print()
    return all_ok


def main():
    """Run all verification checks"""
    print("\n" + "="*70)
    print("RAISN CHATBOT - CODE VERIFICATION")
    print("="*70 + "\n")

    results = {
        'Syntax': check_syntax(),
        'Imports': check_imports(),
        'Database': check_database(),
        'Code Logic': check_code_logic(),
        'Test Queries': check_test_queries(),
        'Documentation': check_documentation(),
    }

    print("="*70)
    print("SUMMARY")
    print("="*70 + "\n")

    for check, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{check:20s}: {status}")

    all_passed = all(results.values())

    print("\n" + "="*70)
    if all_passed:
        print("✅ ALL CHECKS PASSED - CODE IS READY!")
    else:
        print("⚠️  SOME CHECKS FAILED - SEE DETAILS ABOVE")
    print("="*70 + "\n")

    # Additional notes
    print("NEXT STEPS:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Create .env file: cp .env.example .env")
    print("3. Add your OpenRouter API key to .env")
    print("4. Run the app: python app.py")
    print()

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
