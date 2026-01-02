"""
Configuration Module
Contains all system prompts, settings, and model configurations
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# =======================
# MODEL CONFIGURATIONS
# =======================

AVAILABLE_MODELS = {
    "qwen": {
        "id": "qwen/qwen-2.5-72b-instruct",
        "display_name": "Qwen 2.5 (72B)",
        "temperature": 0.3
    },
    "deepseek": {
        "id": "deepseek/deepseek-chat",
        "display_name": "DeepSeek V3",
        "temperature": 0.3
    },
    "deepseek-r1": {
        "id": "deepseek/deepseek-r1",
        "display_name": "DeepSeek R1",
        "temperature": 0.3
    },
    "glm4": {
        "id": "zhipuai/glm-4-9b-chat",
        "display_name": "GLM-4 (9B)",
        "temperature": 0.3
    }
}

DEFAULT_MODEL = "qwen"


# =======================
# API CONFIGURATIONS
# =======================

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_TIMEOUT = 30  # seconds


# =======================
# DATABASE CONFIGURATIONS
# =======================

DB_NAME = "real_estate_data.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)


# =======================
# CHATBOT CONFIGURATIONS
# =======================

MAX_SQL_RETRIES = 2
MAX_CHAT_HISTORY = 20  # Keep last 20 messages for context
RECENT_HISTORY_FOR_ROUTER = 3  # Use last 3 messages for query classification

# =======================
# CLIENT/TENANT CONFIGURATIONS
# =======================

# Available clients (tenants) for POC - in production, this comes from backend
AVAILABLE_CLIENTS = {
    "all": {
        "id": None,  # None means no filtering
        "display_name": "All Clients",
        "description": "View all projects across all clients"
    },
    "casagrand": {
        "id": "TM_TEAM_001",
        "display_name": "Casagrand",
        "description": "Casagrand projects"
    },
    "purvankara": {
        "id": "PURVA_001",
        "display_name": "Purvankara",
        "description": "Purva/Purvankara projects"
    }
}

DEFAULT_CLIENT = "all"  # Default to showing all clients


# =======================
# SYSTEM PROMPTS
# =======================

ROUTER_SYSTEM_PROMPT = """You classify queries for a real estate database chatbot.

ONLY TWO OPTIONS:

1. "general" - ONLY for greetings: "hello", "hi", "hey", "bye", "thank you", "thanks"

2. "data" - EVERYTHING ELSE (default)

If the question mentions: projects, properties, apartments, units, BHK, prices, builders, amenities, locations, construction, or ANYTHING real estate related → MUST be "data"

If you're unsure → classify as "data"

Respond with ONLY ONE WORD: data OR general"""


SQL_GENERATOR_SYSTEM_PROMPT = """You are an expert SQL query generator specializing in SQLite.

Your task is to convert natural language questions into valid SQLite queries.

RULES:
1. Generate ONLY the SQL query - no explanations, no markdown, no code blocks
2. Use proper SQLite syntax
3. Always use table and column names exactly as provided in the schema
4. For counting queries, use COUNT(*)
5. For filtering, use WHERE clauses appropriately
6. If you receive an error, analyze it carefully and fix the issue

CRITICAL PATTERN MATCHING RULES (CASE-INSENSITIVE):
- ALWAYS use LIKE with wildcards for text matching (developer_name, project_name, city names)
- NEVER use = (equals) for developer names, project names, city names, or client names
- ALWAYS make text searches CASE-INSENSITIVE using UPPER() or LOWER()
- Examples:
  * For "Casagrand projects": WHERE UPPER(developer_name) LIKE '%CASAGRAND%'
  * For "Purva projects": WHERE UPPER(developer_name) LIKE '%PURVA%' OR UPPER(project_name) LIKE '%PURVA%'
  * For "Brigade": WHERE UPPER(developer_name) LIKE '%BRIGADE%'
  * For "3bhk units": WHERE UPPER(configuration_type) LIKE '%3BHK%'
  * For "Bangalore" (even if misspelled): WHERE UPPER(city) LIKE '%BANGALORE%'
  * For "Mumbai": WHERE UPPER(city) LIKE '%MUMBAI%'
- Use UPPER() for case-insensitive matching to handle "casagrand", "Casagrand", "CASAGRAND"
- Use = (equals) ONLY for exact matches like IDs, numeric values, or specific status values

FUZZY MATCHING FOR MISSPELLINGS:
- City names: Handle common misspellings (e.g., "bangalor", "mumbay", "chenai")
- Project names: Match partial names from the database (check available projects list)
- Developer names: Match partial or misspelled developer names (check available developers list)
- When user mentions a city/project/developer, refer to the "AVAILABLE DATA IN DATABASE" section to find the correct match

DEVELOPER NAME FILTERING:
- When filtering projects by client/tenant, you can ALSO filter by developer_name
- Example: "Show Purva projects for client Casagrand" → Check if Purva is a developer name and filter accordingly
- Use: WHERE tenant_id = 'TM_TEAM_001' AND UPPER(developer_name) LIKE '%PURVA%'

IMPORTANT: Output ONLY the SQL query, nothing else."""


RESPONSE_SYSTEM_PROMPT = """You are a helpful and friendly assistant.

Your task is to convert database query results into clear, natural language responses.

RULES:
1. Be conversational and friendly
2. Format numbers and data clearly
3. If results are empty, say "I couldn't find any matching records"
4. For multiple results, summarize them concisely
5. Don't include technical SQL details unless asked
6. Be accurate - only state what the data shows

Keep responses clear, concise, and user-friendly."""


GENERAL_CONVERSATION_PROMPT = """You are a friendly assistant for a real estate database chatbot.

Respond ONLY to greetings like "hello", "hi", "thank you", "bye".

For ANY real estate questions, say: "Let me check the database for you."

Be brief and warm."""


# =======================
# ERROR MESSAGES
# =======================

ERROR_MESSAGES = {
    "max_retries": "I apologize, but I'm having trouble processing your data query at the moment. "
                   "This could be due to the complexity of the question or a temporary issue. "
                   "Please try rephrasing your question or try again in a moment.",

    "no_query_result": "I couldn't retrieve the data you requested. "
                       "There was an issue generating or executing the database query. "
                       "Please try rephrasing your question or ask something else.",

    "response_generation": "I apologize, but I'm unable to generate a response right now. "
                          "This might be a temporary issue. Please try again in a moment.",

    "api_timeout": "API request timed out. Please try again.",

    "api_connection": "Unable to connect to the API. Please check your internet connection.",

    "invalid_api_key": "Invalid API key. Please check your OPENROUTER_API_KEY.",

    "rate_limit": "Rate limit exceeded. Please try again in a moment.",

    "unexpected": "Unexpected error occurred: {error}"
}


# =======================
# HELPER FUNCTIONS
# =======================

def get_model_config(model_key: str = None) -> Dict[str, Any]:
    """Get model configuration by key"""
    model_key = model_key or DEFAULT_MODEL
    if model_key not in AVAILABLE_MODELS:
        raise ValueError(f"Unknown model: {model_key}. Available: {list(AVAILABLE_MODELS.keys())}")
    return AVAILABLE_MODELS[model_key]


def validate_config() -> bool:
    """Validate that all required configurations are set"""
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    return True
