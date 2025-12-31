# System Prompts Documentation

This document details all the system prompts used in the LangGraph chatbot for better understanding and customization.

## 1. Router System Prompt

**Purpose**: Classifies user queries into categories (data, general, factual)

**Location**: `ROUTER_SYSTEM_PROMPT` in [app.py](app.py:38-63)

**Key Features**:
- Clear examples for each category
- Strict output format (single word response)
- Handles database queries, general conversation, and factual questions

**Example Classifications**:
- "How many users?" → `data`
- "Hello!" → `general`
- "What is Python?" → `factual`

---

## 2. SQL Generator System Prompt

**Purpose**: Converts natural language to SQLite queries

**Location**: `SQL_GENERATOR_SYSTEM_PROMPT` in [app.py](app.py:65-77)

**Key Features**:
- SQLite-specific syntax rules
- No markdown or code blocks in output
- Error correction guidance for retries
- Schema-aware generation

**Rules**:
1. Generate ONLY the SQL query
2. Use proper SQLite syntax
3. Exact table/column names from schema
4. Use COUNT(*) for counting
5. Proper WHERE clause filtering

---

## 3. Response Synthesizer System Prompt

**Purpose**: Converts SQL results to natural language

**Location**: `RESPONSE_SYSTEM_PROMPT` in [app.py](app.py:79-91)

**Key Features**:
- Conversational and friendly tone
- Clear number formatting
- Empty result handling
- Concise multi-result summaries
- No technical SQL details

**Rules**:
1. Be conversational and friendly
2. Format numbers clearly
3. Handle empty results gracefully
4. Summarize multiple results
5. Only state what data shows

---

## 4. General Conversation System Prompt

**Purpose**: Handles greetings and general chat

**Location**: `GENERAL_CONVERSATION_PROMPT` in [app.py](app.py:93-103)

**Key Features**:
- Warm and professional tone
- Brief, friendly responses
- Context-aware (mentions being a database assistant)
- No fabricated information

**Rules**:
1. Be warm and professional
2. Keep responses brief
3. Mention database assistant role if relevant
4. Don't make up information

---

## User-Friendly Error Messages

### API Errors

**Timeout**:
> "API request timed out. Please try again."

**Connection Error**:
> "Unable to connect to the API. Please check your internet connection."

**Invalid API Key**:
> "Invalid API key. Please check your OPENROUTER_API_KEY."

**Rate Limit**:
> "Rate limit exceeded. Please try again in a moment."

### SQL Errors

**Max Retries Exceeded** (after 2 retry attempts):
> "I apologize, but I'm having trouble processing your data query at the moment. This could be due to the complexity of the question or a temporary issue. Please try rephrasing your question or try again in a moment."

**No Results**:
> "I couldn't retrieve the data you requested. Please try rephrasing your question or ask something else."

### Response Generation Errors

**General Failure**:
> "I apologize, but I'm unable to generate a response right now. This might be a temporary issue. Please try again in a moment."

---

## Error Handling Strategy

### 1. Router Node
- Catches API errors
- Defaults to "general" conversation
- Logs error for debugging

### 2. SQL Generator Node
- Catches generation errors
- Increments retry counter
- Provides error context for retry

### 3. SQL Execution Node
- Catches database errors
- Allows up to 2 retries
- Returns detailed error messages

### 4. Response Node
- Checks for persistent errors
- Provides user-friendly messages
- Never exposes technical details to user

---

## Customization Guide

### Changing Classification Categories

Edit `ROUTER_SYSTEM_PROMPT` to add/modify categories:

```python
ROUTER_SYSTEM_PROMPT = """
...
4. "new_category" - Description
   Examples:
   - "Example 1"
   - "Example 2"
...
"""
```

### Adjusting SQL Generation Rules

Modify `SQL_GENERATOR_SYSTEM_PROMPT` for different SQL dialects:

```python
SQL_GENERATOR_SYSTEM_PROMPT = """
...
RULES:
1. Use PostgreSQL syntax
2. Use LIMIT instead of TOP
...
"""
```

### Customizing Response Tone

Edit `RESPONSE_SYSTEM_PROMPT` for different communication styles:

```python
RESPONSE_SYSTEM_PROMPT = """
...
RULES:
1. Be technical and precise
2. Include SQL details
...
"""
```

### Retry Configuration

Change maximum retry attempts in [app.py](app.py:442):

```python
def check_sql_error(state: AgentState) -> Literal["sql_gen", "response"]:
    if state.get('error') and state.get('retry_count', 0) < 3:  # Change to 3 retries
        return "sql_gen"
    else:
        return "response"
```

---

## Best Practices

1. **Keep prompts concise**: LLMs perform better with clear, focused instructions
2. **Include examples**: Examples help models understand expected output
3. **Specify format**: Always specify exact output format needed
4. **User-friendly errors**: Never expose technical errors to end users
5. **Temperature control**: Use lower temperature (0.3) for consistent results
6. **Timeout handling**: Always set API timeouts (30 seconds default)

---

## Testing Prompts

To test prompt changes:

```python
# Test single model
from app import OpenRouterLLM, ROUTER_SYSTEM_PROMPT

llm = OpenRouterLLM("qwen/qwen-2.5-72b-instruct")
result = llm.invoke("How many users?", ROUTER_SYSTEM_PROMPT)
print(result)  # Should output: data
```

---

## Performance Tips

1. **Router**: Fast classification is critical - keep prompt simple
2. **SQL Generator**: Include schema in system prompt to reduce context
3. **Response**: Use streaming for long responses (future enhancement)
4. **Caching**: Consider caching common queries (future enhancement)
