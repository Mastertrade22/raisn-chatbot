"""
Test script for fuzzy matching functionality
"""

from fuzzy_matching import (
    normalize_city_name,
    find_matching_projects,
    find_matching_developers,
    get_fuzzy_matching_context
)
from database import db_interface


def test_fuzzy_matching():
    """Test fuzzy matching functions"""

    print("=" * 60)
    print("FUZZY MATCHING TEST")
    print("=" * 60)

    # Test 1: Get available data
    print("\n1. AVAILABLE DATA IN DATABASE:")
    print("-" * 60)

    cities = db_interface.get_distinct_cities()
    print(f"\nCities ({len(cities)}): {cities[:10]}")
    if len(cities) > 10:
        print(f"  ... and {len(cities) - 10} more")

    developers = db_interface.get_distinct_developers()
    print(f"\nDevelopers ({len(developers)}): {developers[:10]}")
    if len(developers) > 10:
        print(f"  ... and {len(developers) - 10} more")

    projects = db_interface.get_distinct_project_names()
    print(f"\nProjects ({len(projects)}): {projects[:10]}")
    if len(projects) > 10:
        print(f"  ... and {len(projects) - 10} more")

    # Test 2: Fuzzy matching for developers
    print("\n\n2. DEVELOPER NAME FUZZY MATCHING:")
    print("-" * 60)

    test_developers = ["Casagrand", "casagrand", "Casa", "Purva", "purvankara", "PURVA"]
    for dev_input in test_developers:
        matches = find_matching_developers(dev_input)
        print(f"\nInput: '{dev_input}'")
        print(f"Matches: {matches}")

    # Test 3: Fuzzy matching for projects
    print("\n\n3. PROJECT NAME FUZZY MATCHING:")
    print("-" * 60)

    test_projects = ["Purva", "Casagrand", "Highlands", "zenith"]
    for proj_input in test_projects:
        matches = find_matching_projects(proj_input)
        print(f"\nInput: '{proj_input}'")
        print(f"Matches: {matches[:5]}")  # Show first 5 matches
        if len(matches) > 5:
            print(f"  ... and {len(matches) - 5} more")

    # Test 4: City name normalization (requires LLM)
    print("\n\n4. CITY NAME NORMALIZATION (LLM-based):")
    print("-" * 60)
    print("\nNote: This test requires LLM API access")

    test_cities = ["bangalore", "Bangalore", "BANGALORE", "bangalor", "mumbay", "Mumbai"]
    for city_input in test_cities:
        try:
            normalized = normalize_city_name(city_input)
            print(f"\nInput: '{city_input}' → Normalized: '{normalized}'")
        except Exception as e:
            print(f"\nInput: '{city_input}' → Error: {str(e)}")

    # Test 5: Get fuzzy matching context for SQL generation
    print("\n\n5. FUZZY MATCHING CONTEXT FOR SQL GENERATION:")
    print("-" * 60)

    context = get_fuzzy_matching_context()
    print(context)

    print("\n\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    test_fuzzy_matching()
