"""
Fuzzy Matching Module
Handles fuzzy matching for cities, projects, and developers using LLM and database lookups
"""

from typing import Optional, List, Dict
from llm_client import create_llm_client
from database import db_interface


def normalize_city_name(city_input: str, model_name: str = "qwen/qwen-2.5-72b-instruct") -> str:
    """
    Use LLM to normalize misspelled city names to correct spelling

    Args:
        city_input: The potentially misspelled city name
        model_name: LLM model to use for normalization

    Returns:
        str: Normalized city name
    """
    # Get list of cities from database
    known_cities = db_interface.get_distinct_cities()

    if not known_cities:
        # No cities in database, return original input
        return city_input

    # Check if it's already an exact match (case-insensitive)
    for city in known_cities:
        if city.lower() == city_input.lower():
            return city

    # Use LLM to find the best match
    llm = create_llm_client(model_name)

    cities_list = ", ".join(known_cities)

    system_prompt = """You are a city name normalizer. Given a potentially misspelled city name and a list of valid cities, return ONLY the correct city name from the list that best matches the input.

Rules:
1. Return ONLY the city name, nothing else
2. If the input doesn't match any city in the list, return the original input
3. Handle common misspellings (e.g., "bangalor" -> "Bangalore", "mumbay" -> "Mumbai")
4. Be case-insensitive in matching"""

    prompt = f"""Input city name: {city_input}
Valid cities: {cities_list}

Correct city name:"""

    try:
        normalized_city = llm.invoke(prompt, system_prompt).strip()

        # Verify the result is in our list of cities
        for city in known_cities:
            if city.lower() == normalized_city.lower():
                return city

        # If LLM returned something not in our list, return original
        return city_input

    except Exception as e:
        print(f"Error normalizing city name: {e}")
        return city_input


def find_matching_projects(project_input: str, tenant_id: Optional[str] = None) -> List[str]:
    """
    Find project names from database that match the input (fuzzy matching)

    Args:
        project_input: The project name or partial name to search for
        tenant_id: Optional tenant ID for filtering

    Returns:
        List[str]: List of matching project names from database
    """
    known_projects = db_interface.get_distinct_project_names(tenant_id)

    if not known_projects:
        return []

    # Simple fuzzy matching: case-insensitive substring matching
    matches = []
    project_input_lower = project_input.lower()

    for project in known_projects:
        if project_input_lower in project.lower() or project.lower() in project_input_lower:
            matches.append(project)

    return matches


def find_matching_developers(developer_input: str, tenant_id: Optional[str] = None) -> List[str]:
    """
    Find developer names from database that match the input (fuzzy matching)

    Args:
        developer_input: The developer name or partial name to search for
        tenant_id: Optional tenant ID for filtering

    Returns:
        List[str]: List of matching developer names from database
    """
    known_developers = db_interface.get_distinct_developers(tenant_id)

    if not known_developers:
        return []

    # Simple fuzzy matching: case-insensitive substring matching
    matches = []
    developer_input_lower = developer_input.lower()

    for developer in known_developers:
        if developer_input_lower in developer.lower() or developer.lower() in developer_input_lower:
            matches.append(developer)

    return matches


def get_fuzzy_matching_context(tenant_id: Optional[str] = None) -> str:
    """
    Get fuzzy matching context for SQL generation including available cities, projects, and developers

    Args:
        tenant_id: Optional tenant ID for filtering

    Returns:
        str: Formatted context for LLM
    """
    cities = db_interface.get_distinct_cities()
    projects = db_interface.get_distinct_project_names(tenant_id)
    developers = db_interface.get_distinct_developers(tenant_id)

    context = "\nAVAILABLE DATA IN DATABASE:\n"

    if cities:
        context += f"\nCities: {', '.join(cities[:20])}"  # Limit to first 20 for token efficiency
        if len(cities) > 20:
            context += f" (and {len(cities) - 20} more)"

    if developers:
        context += f"\n\nDevelopers: {', '.join(developers[:20])}"
        if len(developers) > 20:
            context += f" (and {len(developers) - 20} more)"

    if projects:
        context += f"\n\nProjects: {', '.join(projects[:30])}"
        if len(projects) > 30:
            context += f" (and {len(projects) - 30} more)"

    context += "\n\nIMPORTANT: Use LIKE with wildcards for fuzzy matching on these names."

    return context
