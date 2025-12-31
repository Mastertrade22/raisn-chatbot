# Real Estate Chatbot - Modular Architecture ✅

> **Production-ready chatbot with clean separation of concerns**

This is a refactored, modular version of the real estate chatbot that separates:
- ✅ **Core chatbot logic** (production-ready)
- ✅ **Frontend/UI** (Streamlit, CLI)
- ✅ **Configuration** (centralized)
- ✅ **Database** (abstracted interface)

## 🚀 Quick Start (5 minutes)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
# Create .env file
echo "OPENROUTER_API_KEY=your_api_key_here" > .env
```

### 3. Test Everything

```bash
# Run comprehensive tests
python test_refactored.py
```

Expected output:
```
✅ PASS - imports
✅ PASS - config
✅ PASS - database
✅ PASS - llm_client
✅ PASS - chatbot_core

Results: 5/5 tests passed

🎉 All tests passed! Your refactored code is ready to use.
```

### 4. Try the CLI Demo

```bash
python demo_cli.py
```

### 5. Try the Web UI

```bash
streamlit run streamlit_app_new.py
```

## 📁 Project Structure

### 🎯 Core Modules (Production)

These are the modules you'll use in production:

```
chatbot_core.py      # Main chatbot with LangGraph workflow
config.py            # All configurations, prompts, settings
database.py          # Database interface and operations
llm_client.py        # LLM API client with error handling
real_estate_db.py    # Database setup and schema
```

### 🎨 Demo/Frontend Modules

For testing and reference:

```
demo_cli.py          # Interactive CLI demo
streamlit_app_new.py # Modern Streamlit web UI
production_example.py # Integration examples (FastAPI, Flask, Lambda)
test_refactored.py   # Comprehensive test suite
```

### 📚 Documentation

```
QUICKSTART_NEW.md         # Quick start guide
ARCHITECTURE.md           # Complete architecture guide
REFACTORING_SUMMARY.md    # Before/after comparison
README_NEW.md             # This file
```

### 📦 Legacy Files (Reference Only)

```
app.py               # Original monolithic script
streamlit_app.py     # Original Streamlit UI
```

## 💡 Usage Examples

### Example 1: Simple Python Integration

```python
from chatbot_core import create_chatbot

# Initialize
chatbot = create_chatbot()

# Ask questions
response = chatbot.ask("How many projects are under construction?")
print(response['final_answer'])
# Output: "There are 3 projects currently under construction."
```

### Example 2: FastAPI Integration

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

Run with: `uvicorn your_app:app --reload`

### Example 3: With History

```python
chatbot = create_chatbot()

# Conversation with context
chatbot.ask("How many projects are there?")
chatbot.ask("Which ones are in Bangalore?")  # Uses context

# Clear history when needed
chatbot.reset_history()
```

### Example 4: Detailed Response

```python
response = chatbot.ask("Show me 2BHK apartments")

print(f"Answer: {response['final_answer']}")
print(f"Type: {response['query_type']}")     # "data" or "general"
print(f"SQL: {response['sql_query']}")        # Generated SQL query
print(f"Error: {response['error']}")          # Error if any
```

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│       Frontend Layer                │
│  ┌──────────┐  ┌──────────────┐    │
│  │Streamlit │  │     CLI      │    │
│  └──────────┘  └──────────────┘    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│       Core Chatbot Layer            │
│  ┌─────────────────────────────┐   │
│  │    chatbot_core.py          │   │
│  │  • RealEstateChatbot class  │   │
│  │  • LangGraph workflow       │   │
│  │  • ask() method             │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
         ↓        ↓        ↓
┌──────────┐ ┌──────────┐ ┌──────────┐
│LLM Client│ │ Database │ │  Config  │
└──────────┘ └──────────┘ └──────────┘
```

### LangGraph Workflow

```
User Question
    ↓
Router (classify: data vs general)
    ↓
SQL Generator (if data query)
    ↓
Execute SQL (with retry logic)
    ↓
Response Synthesizer
    ↓
Final Answer
```

## ⚙️ Configuration

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=sk-or-v1-xxxxx

# Optional (has defaults)
DEFAULT_MODEL=qwen
MAX_SQL_RETRIES=2
API_TIMEOUT=30
```

### Customize Models

Edit [config.py](config.py):

```python
AVAILABLE_MODELS = {
    "your_model": {
        "id": "provider/model-name",
        "display_name": "Your Model",
        "temperature": 0.3
    }
}
```

### Customize Prompts

Edit [config.py](config.py):

```python
ROUTER_SYSTEM_PROMPT = """Your custom prompt"""
SQL_GENERATOR_SYSTEM_PROMPT = """Your custom prompt"""
RESPONSE_SYSTEM_PROMPT = """Your custom prompt"""
```

## 🧪 Testing

### Run All Tests

```bash
python test_refactored.py
```

### Run CLI Demo

```bash
# Interactive mode
python demo_cli.py

# Batch mode
python demo_cli.py --batch
```

### Run Web UI

```bash
streamlit run streamlit_app_new.py
```

### Test in Python REPL

```python
from chatbot_core import create_chatbot

chatbot = create_chatbot()
response = chatbot.ask("How many projects?")
print(response['final_answer'])
```

## 🚢 Production Deployment

### Option 1: Direct Import (Simplest)

```python
# your_production_app.py
from chatbot_core import create_chatbot

chatbot = create_chatbot()

def handle_user_query(user_input: str) -> str:
    response = chatbot.ask(user_input)
    return response['final_answer']
```

### Option 2: REST API

See [production_example.py](production_example.py) for:
- FastAPI example
- Flask example
- AWS Lambda handler

### Option 3: Serverless

Package and deploy to:
- AWS Lambda
- Google Cloud Functions
- Azure Functions

See [production_example.py](production_example.py) for Lambda handler.

## 📊 Response Format

```python
{
    'final_answer': 'There are 71 real estate projects in the database.',
    'query_type': 'data',  # or 'general'
    'sql_query': 'SELECT COUNT(*) FROM projects',
    'error': ''  # Empty if no error
}
```

## 🔍 Troubleshooting

### "Invalid API key"

Check your `.env` file:
```bash
cat .env | grep OPENROUTER_API_KEY
```

### "Database not found"

Database is created automatically. If issues persist:
```python
from database import db_interface
db_interface.test_connection()
```

### "Module not found"

Install dependencies:
```bash
pip install -r requirements.txt
```

### Import errors

Make sure you're in the project directory:
```bash
cd raisn_chatbot
python demo_cli.py
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [QUICKSTART_NEW.md](QUICKSTART_NEW.md) | Quick start guide with examples |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Complete architecture documentation |
| [REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md) | Before/after comparison |
| [production_example.py](production_example.py) | Integration examples |

## ✨ Key Features

- ✅ **Production-ready**: Clean API, error handling, no side effects
- ✅ **Modular**: Separate concerns, easy to maintain
- ✅ **Flexible**: Works with any frontend (Streamlit, CLI, API)
- ✅ **Configurable**: All settings in one place
- ✅ **Testable**: Comprehensive test suite included
- ✅ **Well-documented**: Multiple guides and examples

## 🎯 Comparison with Legacy Code

| Aspect | Legacy (app.py) | New (Modular) |
|--------|------------------|---------------|
| Setup complexity | 8+ fields to configure | 1 function call |
| Reusability | ❌ Hard to reuse | ✅ Import and use |
| Configuration | ❌ Hardcoded | ✅ Centralized |
| Production ready | ❌ Needs work | ✅ Ready now |
| Documentation | ⚠️ Basic | ✅ Comprehensive |

## 🎓 Learning Path

1. **Beginner**: Run `demo_cli.py`, try simple integration
2. **Intermediate**: Run `streamlit_app_new.py`, customize config
3. **Advanced**: Read `ARCHITECTURE.md`, deploy to production

## 💼 Use Cases

- **Internal Tool**: Use CLI or Streamlit UI
- **API Service**: Deploy FastAPI/Flask wrapper
- **Embedded**: Import directly into your Python app
- **Serverless**: Deploy to Lambda/Cloud Functions
- **Mobile Backend**: Create REST API

## 🤝 Contributing

When making changes:
1. Keep core modules (chatbot_core, config, database, llm_client) pure
2. Add UI-specific code to separate files
3. Update tests in `test_refactored.py`
4. Update documentation

## 📞 Support

- **Quick questions**: See [QUICKSTART_NEW.md](QUICKSTART_NEW.md)
- **Architecture questions**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Integration help**: See [production_example.py](production_example.py)
- **Test issues**: Run `python test_refactored.py`

## 🎉 Ready to Go!

Your chatbot is production-ready! Start with:

```bash
# Test everything
python test_refactored.py

# Try the CLI
python demo_cli.py

# Try the web UI
streamlit run streamlit_app_new.py

# Use in your code
from chatbot_core import create_chatbot
chatbot = create_chatbot()
response = chatbot.ask("Your question")
```

---

**Built with:** LangGraph, OpenRouter API, SQLite, Streamlit

**License:** [Your License]

**Version:** 2.0 (Modular)
