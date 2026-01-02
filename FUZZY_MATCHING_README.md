# Fuzzy Matching Implementation

This document describes the fuzzy matching capabilities added to the real estate chatbot.

## Overview

The chatbot now handles misspellings and partial matches for:
- **City names** (using LLM intelligence)
- **Project names** (using database lookups)
- **Developer names** (using database lookups)

## Features

### 1. City Name Fuzzy Matching (LLM-based)

The chatbot uses LLM to understand and normalize misspelled city names.

**Examples:**
- "bangalor" → "Bangalore"
- "mumbay" → "Mumbai"
- "chenai" → "Chennai"
- "delhee" → "Delhi"

**How it works:**
- Retrieves all distinct cities from the database
- Uses LLM to match the misspelled input to the correct city name
- Falls back to original input if no match is found

### 2. Project Name Fuzzy Matching (Database-based)

The chatbot matches partial or misspelled project names using database lookups.

**Examples:**
- "Purva" → Matches "Purva Highlands", "Purva Zenith", etc.
- "zenith" → Matches "Purva Zenith", "Zenith Towers", etc.
- "highlands" → Matches "Purva Highlands"

**How it works:**
- Retrieves all distinct project names from the database
- Performs case-insensitive substring matching
- Returns all matching projects

### 3. Developer Name Fuzzy Matching (Database-based)

The chatbot matches developer names flexibly, allowing partial matches and case variations.

**Examples:**
- "Casagrand" → Matches "Casagrand Builders"
- "casagrand" → Matches "Casagrand Builders" (case-insensitive)
- "Purva" → Matches "Purvankara Limited"
- "purvankara" → Matches "Purvankara Limited"

**How it works:**
- Retrieves all distinct developer names from the database
- Performs case-insensitive substring matching
- Can be filtered by tenant_id for multi-tenant scenarios

### 4. Developer Name Filtering

Projects can now be filtered by developer name, even when filtering by client/tenant.

**Examples:**
- "Show Purva projects" → Filters by developer_name LIKE '%PURVA%'
- "Show Casagrand projects for client ABC" → Filters by both tenant_id and developer_name
- "How many projects does Purva have?" → Counts projects by developer

**SQL Generation:**
```sql
-- Filter by developer only
SELECT * FROM projects WHERE UPPER(developer_name) LIKE '%PURVA%'

-- Filter by tenant and developer
SELECT * FROM projects
WHERE tenant_id = 'TM_TEAM_001'
  AND UPPER(developer_name) LIKE '%PURVA%'
```

## Implementation Details

### Files Modified

1. **database.py**
   - Added `get_distinct_cities()` - Get all cities from database
   - Added `get_distinct_developers(tenant_id)` - Get all developers
   - Added `get_distinct_project_names(tenant_id)` - Get all project names

2. **fuzzy_matching.py** (NEW)
   - `normalize_city_name(city_input, model_name)` - LLM-based city normalization
   - `find_matching_projects(project_input, tenant_id)` - Database lookup for projects
   - `find_matching_developers(developer_input, tenant_id)` - Database lookup for developers
   - `get_fuzzy_matching_context(tenant_id)` - Get context for SQL generation

3. **chatbot_core.py**
   - Modified `sql_gen_node()` to include fuzzy matching context
   - Context includes available cities, projects, and developers

4. **config.py**
   - Updated `SQL_GENERATOR_SYSTEM_PROMPT` with fuzzy matching instructions
   - Added guidelines for handling misspellings
   - Added rules for developer name filtering

### SQL Query Pattern Matching

All text searches now use case-insensitive LIKE queries:

```sql
-- City matching (handles misspellings)
WHERE UPPER(city) LIKE '%BANGALORE%'

-- Project name matching (handles partial names)
WHERE UPPER(project_name) LIKE '%PURVA%'

-- Developer name matching (handles variants)
WHERE UPPER(developer_name) LIKE '%CASAGRAND%'

-- Configuration type matching (case-insensitive)
WHERE UPPER(configuration_type) LIKE '%3BHK%'
```

**NEVER use `=` for text matching**, always use `LIKE` with wildcards.

## Usage Examples

### Basic Usage

```python
from chatbot_core import create_chatbot

# Create chatbot
bot = create_chatbot()

# Query with misspelled city
response = bot.ask("Show me projects in bangalor")

# Query with partial project name
response = bot.ask("Tell me about Purva projects")

# Query with developer name
response = bot.ask("How many projects does Casagrand have?")
```

### With Tenant Filtering

```python
# Create chatbot with tenant context
bot = create_chatbot(tenant_id="TM_TEAM_001")

# Developer filtering within tenant
response = bot.ask("Show Purva projects")
# SQL: WHERE tenant_id = 'TM_TEAM_001' AND UPPER(developer_name) LIKE '%PURVA%'
```

### Testing

Run the test script to verify fuzzy matching:

```bash
python test_fuzzy_matching.py
```

Run example queries:

```bash
python example_fuzzy_queries.py
```

## Configuration

### LLM Model for City Normalization

The default model is `qwen/qwen-2.5-72b-instruct`. You can change it by modifying the `normalize_city_name()` function call:

```python
from fuzzy_matching import normalize_city_name

# Use different model
normalized = normalize_city_name("bangalor", model_name="deepseek/deepseek-chat")
```

### Fuzzy Matching Context Limits

To optimize token usage, the fuzzy matching context limits the number of items shown to the LLM:
- Cities: First 20
- Developers: First 20
- Projects: First 30

You can modify these limits in `fuzzy_matching.py`:

```python
def get_fuzzy_matching_context(tenant_id: Optional[str] = None) -> str:
    # Change these values to adjust limits
    context += f"\nCities: {', '.join(cities[:20])}"  # Change 20 to your limit
    context += f"\n\nDevelopers: {', '.join(developers[:20])}"
    context += f"\n\nProjects: {', '.join(projects[:30])}"
```

## Benefits

1. **Better User Experience**: Users don't need to spell names exactly
2. **More Flexible Queries**: Partial names and variations work
3. **Reduced Errors**: Less "no results found" due to typos
4. **Multi-tenant Support**: Fuzzy matching works with tenant filtering
5. **Case-Insensitive**: All matching is case-insensitive by default

## Limitations

1. **LLM Dependency**: City normalization requires LLM API access
2. **Token Usage**: Fuzzy matching context adds tokens to each query
3. **Exact Matches**: Very specific searches might match too broadly
4. **Database Size**: Large databases may exceed context limits

## Future Improvements

1. **Phonetic Matching**: Add soundex or metaphone for better phonetic matches
2. **Edit Distance**: Implement Levenshtein distance for closer matches
3. **Caching**: Cache normalized city names to reduce LLM calls
4. **User Feedback**: Allow users to correct/confirm matches
5. **Synonym Support**: Handle synonyms (e.g., "Bengaluru" vs "Bangalore")

## Troubleshooting

### City normalization not working
- Check if OPENROUTER_API_KEY is set in .env
- Verify LLM client is working: `python test_refactored.py`
- Check if cities exist in database: `python test_fuzzy_matching.py`

### No matches found for projects/developers
- Verify data exists in database
- Check tenant_id filtering is correct
- Run `python test_fuzzy_matching.py` to see available data

### SQL queries still failing
- Check database schema matches expected structure
- Verify LIKE queries are being used (not =)
- Review generated SQL in chatbot response

## Summary

The fuzzy matching implementation makes the chatbot more user-friendly by:
- Understanding misspelled city names using LLM intelligence
- Matching partial project and developer names from the database
- Supporting case-insensitive text matching throughout
- Enabling developer-based filtering alongside tenant filtering

All text matching now uses `UPPER() + LIKE '%...%'` pattern for maximum flexibility.
