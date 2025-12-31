# Real Estate Chatbot - Modular Architecture

## Overview

This codebase has been restructured into a **modular, production-ready architecture** that separates concerns between:
- **Core chatbot logic** (LangGraph + LLM)
- **Frontend/UI** (Streamlit, CLI, or any other interface)
- **Deployment** (can be easily deployed to various platforms)

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Streamlit   │  │     CLI      │  │  Production  │  │
│  │     UI       │  │     Demo     │  │   API/Web    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                    CORE CHATBOT LAYER                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │         chatbot_core.py                         │   │
│  │  • RealEstateChatbot class                      │   │
│  │  • LangGraph workflow                           │   │
│  │  • Production-ready ask() method                │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   LLM Client │  │   Database   │  │    Config    │
│              │  │   Interface  │  │              │
│ llm_client.py│  │ database.py  │  │  config.py   │
└──────────────┘  └──────────────┘  └──────────────┘
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  OpenRouter  │  │   SQLite DB  │  │ Environment  │
│     API      │  │              │  │  Variables   │
└──────────────┘  └──────────────┘  └──────────────┘
```

## File Structure

### Core Modules (Production-Ready)

```
chatbot_core.py         # Main chatbot logic - plug this into production
├── RealEstateChatbot   # Production-ready chatbot class
├── create_chatbot()    # Factory function
└── LangGraph workflow  # Router → SQL Gen → Execute → Response

config.py               # All configurations and prompts
├── Model configurations
├── System prompts
├── Error messages
└── Settings (retries, timeouts, etc.)

database.py             # Database interface
├── DatabaseInterface class
├── execute_query()
├── get_schema()
└── Connection management

llm_client.py           # LLM API client
├── OpenRouterLLM class
├── Error handling
└── API communication
```

### Frontend/Demo Modules

```
streamlit_app_new.py    # Modern Streamlit UI
demo_cli.py             # CLI demo for testing
app.py                  # Legacy script (keep for reference)
streamlit_app.py        # Legacy Streamlit (keep for reference)
```

### Database Modules

```
real_estate_db.py       # Database setup and schema
real_estate_data.db     # SQLite database file
```

## Key Design Principles

### 1. Separation of Concerns
- **Core chatbot** (`chatbot_core.py`) has NO UI dependencies
- **Frontend** (Streamlit, CLI) only handles display
- **Configuration** (`config.py`) is centralized and easy to modify

### 2. Production-Ready
- Clean API: `chatbot.ask(question)` returns structured response
- Error handling at every layer
- No print statements in core modules
- Proper logging (can be added easily)

### 3. Plug-and-Play
The chatbot can be plugged into ANY application:

```python
from chatbot_core import create_chatbot

# Initialize
chatbot = create_chatbot(model_id="qwen/qwen-2.5-72b-instruct")

# Use it
response = chatbot.ask("How many projects are under construction?")
print(response['final_answer'])
```

### 4. Easy Configuration
All settings in one place (`config.py`):
- Change models
- Modify prompts
- Adjust retry logic
- Update error messages

## Usage Examples

### Example 1: CLI Demo

```bash
python demo_cli.py
```

Interactive CLI that demonstrates core functionality.

### Example 2: Streamlit UI

```bash
streamlit run streamlit_app_new.py
```

Modern web interface with model comparison.

### Example 3: Production Integration

```python
# In your production code
from chatbot_core import create_chatbot

# Initialize once (e.g., at app startup)
chatbot = create_chatbot()

# Use in your endpoint/handler
def handle_user_query(user_question: str):
    response = chatbot.ask(user_question)
    return {
        "answer": response['final_answer'],
        "query_type": response['query_type'],
        "metadata": {
            "sql": response.get('sql_query', '')
        }
    }
```

### Example 4: FastAPI Integration

```python
from fastapi import FastAPI
from chatbot_core import create_chatbot

app = FastAPI()
chatbot = create_chatbot()

@app.post("/chat")
async def chat(question: str):
    response = chatbot.ask(question)
    return response
```

### Example 5: Flask Integration

```python
from flask import Flask, request, jsonify
from chatbot_core import create_chatbot

app = Flask(__name__)
chatbot = create_chatbot()

@app.route('/chat', methods=['POST'])
def chat():
    question = request.json.get('question')
    response = chatbot.ask(question)
    return jsonify(response)
```

## Deployment Strategies

### Strategy 1: Standalone Service
Deploy `chatbot_core.py` as a microservice:
- FastAPI/Flask wrapper
- Docker container
- Kubernetes deployment
- Expose REST API

### Strategy 2: Embedded Library
Import directly into your application:
- Add as Python module
- Configure via environment variables
- Call `chatbot.ask()` from your code

### Strategy 3: Serverless
Deploy as serverless function:
- AWS Lambda
- Google Cloud Functions
- Azure Functions
- API Gateway

## Configuration

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=your_api_key_here

# Optional (has defaults in config.py)
DB_PATH=/path/to/database.db
DEFAULT_MODEL=qwen
MAX_SQL_RETRIES=2
API_TIMEOUT=30
```

### Changing Models

Edit `config.py`:

```python
AVAILABLE_MODELS = {
    "your_model": {
        "id": "provider/model-name",
        "display_name": "Your Model",
        "temperature": 0.3
    }
}
```

### Customizing Prompts

Edit `config.py`:

```python
ROUTER_SYSTEM_PROMPT = """Your custom prompt here"""
SQL_GENERATOR_SYSTEM_PROMPT = """Your custom prompt here"""
RESPONSE_SYSTEM_PROMPT = """Your custom prompt here"""
```

## Testing

### Test Core Functionality

```bash
# Interactive CLI
python demo_cli.py

# Batch test
python demo_cli.py --batch
```

### Test in Python

```python
from chatbot_core import create_chatbot

chatbot = create_chatbot()

# Test question
response = chatbot.ask("How many projects are under construction?")

print(f"Answer: {response['final_answer']}")
print(f"Type: {response['query_type']}")
print(f"SQL: {response['sql_query']}")
```

## Migration Guide

### From Legacy `app.py` to New Architecture

**Before:**
```python
from app import create_graph, compare_models

graph = create_graph(model_id)
final_state = graph.invoke(initial_state)
answer = final_state['final_answer']
```

**After:**
```python
from chatbot_core import create_chatbot

chatbot = create_chatbot(model_id)
response = chatbot.ask(question)
answer = response['final_answer']
```

## Advantages of New Architecture

1. **Modularity**: Each component has a single responsibility
2. **Testability**: Easy to unit test individual modules
3. **Maintainability**: Changes in one module don't affect others
4. **Scalability**: Core chatbot can be scaled independently
5. **Flexibility**: Easy to swap out components (LLM, database, UI)
6. **Production-Ready**: Clean API, error handling, no side effects

## Next Steps

1. **Add Logging**: Integrate proper logging framework
2. **Add Metrics**: Track usage, latency, errors
3. **Add Caching**: Cache frequent queries
4. **Add Authentication**: Secure API endpoints
5. **Add Rate Limiting**: Prevent abuse
6. **Add Monitoring**: Health checks, alerts

## Support

For questions or issues:
1. Check `demo_cli.py` for usage examples
2. Review `config.py` for configuration options
3. Read inline documentation in `chatbot_core.py`
