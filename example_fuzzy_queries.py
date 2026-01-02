"""
Example queries demonstrating fuzzy matching capabilities
Shows how the chatbot handles misspelled cities, projects, and developer names
"""

from chatbot_core import create_chatbot


def run_fuzzy_matching_examples():
    """Run example queries with fuzzy matching"""

    print("=" * 80)
    print("FUZZY MATCHING EXAMPLES FOR REAL ESTATE CHATBOT")
    print("=" * 80)

    # Create chatbot instance
    bot = create_chatbot()

    # Example queries demonstrating fuzzy matching
    examples = [
        {
            "category": "MISSPELLED CITY NAMES",
            "queries": [
                "Show me projects in bangalor",  # Misspelled Bangalore
                "What projects are in mumbay?",  # Misspelled Mumbai
                "List all projects in chenai",  # Misspelled Chennai
                "Projects in pune",  # Correct spelling
            ]
        },
        {
            "category": "FUZZY PROJECT NAME MATCHING",
            "queries": [
                "Tell me about Purva projects",  # Partial name
                "Show Casagrand projects",  # Exact developer name
                "What are the Zenith projects?",  # Partial project name
                "Show me highlands projects",  # Partial name, lowercase
            ]
        },
        {
            "category": "DEVELOPER NAME FILTERING",
            "queries": [
                "Show me all Casagrand projects",
                "List projects by purva",  # Lowercase
                "How many projects does PURVA have?",  # Uppercase
                "Show purvankara projects",  # Full name variant
            ]
        },
        {
            "category": "COMBINED FILTERING (Developer + Client/Tenant)",
            "queries": [
                "Show Purva projects for Casagrand client",
                "List all projects by Casagrand developer",
                "What Purva projects are under Purvankara tenant?",
            ]
        },
        {
            "category": "CASE-INSENSITIVE MATCHING",
            "queries": [
                "Show me 3BHK units",
                "List 3bhk apartments",  # Lowercase
                "Find 2BHK units",
                "Show all 4bhk properties",
            ]
        }
    ]

    for example_group in examples:
        print(f"\n{'=' * 80}")
        print(f"{example_group['category']}")
        print('=' * 80)

        for query in example_group['queries']:
            print(f"\n📝 QUERY: {query}")
            print("-" * 80)

            try:
                response = bot.ask(query, preserve_history=False)

                print(f"Query Type: {response['query_type']}")
                if response.get('sql_query'):
                    print(f"\nGenerated SQL:\n{response['sql_query']}")
                print(f"\n💬 RESPONSE:\n{response['final_answer']}")

                if response.get('error'):
                    print(f"\n⚠️  ERROR: {response['error']}")

            except Exception as e:
                print(f"\n❌ ERROR: {str(e)}")

            print()

    print("\n" + "=" * 80)
    print("EXAMPLES COMPLETED")
    print("=" * 80)


def demonstrate_developer_filtering():
    """Demonstrate developer filtering with tenant context"""

    print("\n\n" + "=" * 80)
    print("DEVELOPER FILTERING WITH TENANT CONTEXT")
    print("=" * 80)

    # Create chatbot with specific tenant
    bot = create_chatbot(tenant_id="TM_TEAM_001")  # Casagrand tenant

    queries = [
        "Show all projects",  # Should show only Casagrand tenant projects
        "Show Purva projects",  # Should filter by developer within tenant
        "How many projects do we have?",  # Should count tenant projects
        "List projects by Casagrand",  # Should match developer name
    ]

    for query in queries:
        print(f"\n📝 QUERY (Tenant: TM_TEAM_001): {query}")
        print("-" * 80)

        try:
            response = bot.ask(query, preserve_history=False)

            if response.get('sql_query'):
                print(f"\nGenerated SQL:\n{response['sql_query']}")
            print(f"\n💬 RESPONSE:\n{response['final_answer']}")

        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}")

        print()


if __name__ == "__main__":
    print("\n🏗️  Starting Fuzzy Matching Examples...\n")

    # Run examples
    run_fuzzy_matching_examples()

    # Demonstrate developer filtering
    demonstrate_developer_filtering()

    print("\n✅ All examples completed!")
    print("\nKEY FEATURES DEMONSTRATED:")
    print("  1. Misspelled city names are handled using LLM normalization")
    print("  2. Project names are matched fuzzily using database lookups")
    print("  3. Developer names can be used to filter projects")
    print("  4. All text matching is case-insensitive")
    print("  5. Tenant/client filtering works alongside developer filtering")
    print()
