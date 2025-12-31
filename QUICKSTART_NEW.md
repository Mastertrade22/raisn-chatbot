# Quick Start Guide - Modular Chatbot

## 🚀 Getting Started in 5 Minutes

### 1. Installation

```bash
# Navigate to project directory
cd raisn_chatbot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY
```

### 2. Test the Core Chatbot (CLI)

```bash
# Run the CLI demo
python demo_cli.py
```

You'll see:
```
🏠 Real Estate AI Chatbot - CLI Demo
====================================

📁 Checking database...
✅ Database connected: 5 projects, 20 units

🤖 Available Models:
  1. Qwen 2.5 (72B)
  2. DeepSeek V3

Select model (1-2) [default: 1]:

✅ Using model: qwen/qwen-2.5-72b-instruct
✅ Chatbot ready!

👤 You:
```

Try asking:
- "How many projects are under construction?"
- "Show me all 3BHK units"
- "What is the cheapest apartment?"

### 3. Test the Web UI (Streamlit)

```bash
# Run the new Streamlit app
streamlit run streamlit_app_new.py
```

Opens in browser at `http://localhost:8501`

### 4. Use in Your Python Code

```python
from chatbot_core import create_chatbot

# Initialize
chatbot = create_chatbot()

# Ask questions
response = chatbot.ask("How many projects are under construction?")

print(response['final_answer'])
# Output: "There are 3 projects currently under construction."
```

## 📁 Project Structure

### Core Modules (Use These in Production)

| File | Purpose | Import In Production? |
|------|---------|----------------------|
| `chatbot_core.py` | Main chatbot logic | ✅ YES |
| `config.py` | Configuration & prompts | ✅ YES |
| `database.py` | Database interface | ✅ YES |
| `llm_client.py` | LLM API client | ✅ YES |
| `real_estate_db.py` | Database setup | ✅ YES |

### Demo/Frontend Modules (For Reference/Testing)

| File | Purpose | Import In Production? |
|------|---------|----------------------|
| `demo_cli.py` | CLI demo | ❌ NO (demo only) |
| `streamlit_app_new.py` | Web UI | ❌ NO (frontend) |
| `production_example.py` | Integration examples | ❌ NO (examples) |

### Legacy Files (Keep for Reference)

| File | Purpose |
|------|---------|
| `app.py` | Old monolithic script |
| `streamlit_app.py` | Old Streamlit UI |

## 🔧 Core API Usage

### Initialize Chatbot

```python
from chatbot_core import create_chatbot

# With default model (Qwen)
chatbot = create_chatbot()

# With specific model
chatbot = create_chatbot(model_id="deepseek/deepseek-chat")
```

### Ask Questions

```python
# Simple usage
response = chatbot.ask("How many projects are there?")
print(response['final_answer'])

# With full response details
response = chatbot.ask("Show me 2BHK apartments")
print(f"Answer: {response['final_answer']}")
print(f"Type: {response['query_type']}")  # "data" or "general"
print(f"SQL: {response['sql_query']}")     # Generated SQL query
```

### Manage Chat History

```python
# Chat history is preserved by default
chatbot.ask("How many projects?")
chatbot.ask("Which ones are in Bangalore?")  # Uses context

# Disable history for a single query
response = chatbot.ask("Hello!", preserve_history=False)

# Clear history
chatbot.reset_history()

# Get history
history = chatbot.get_history()
for msg in history:
    print(f"{msg['role']}: {msg['content']}")
```

## 🎯 Production Integration

### Option 1: Direct Import (Simplest)

```python
# your_app.py
from chatbot_core import create_chatbot

chatbot = create_chatbot()

def handle_user_query(user_input: str) -> str:
    response = chatbot.ask(user_input)
    return response['final_answer']
```

### Option 2: REST API (FastAPI)

```python
# api.py
from fastapi import FastAPI
from chatbot_core import create_chatbot

app = FastAPI()
chatbot = create_chatbot()

@app.post("/chat")
async def chat(question: str):
    response = chatbot.ask(question)
    return response
```

Run with: `uvicorn api:app --reload`

### Option 3: Flask API

See `production_example.py` for complete Flask example.

### Option 4: AWS Lambda

See `production_example.py` for Lambda handler example.

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:

```bash
# Required
OPENROUTER_API_KEY=sk-or-v1-xxxxx

# Optional (has defaults)
DEFAULT_MODEL=qwen
MAX_SQL_RETRIES=2
API_TIMEOUT=30
```

### Customize Models

Edit `config.py`:

```python
AVAILABLE_MODELS = {
    "my_model": {
        "id": "provider/model-name",
        "display_name": "My Model",
        "temperature": 0.3
    }
}
```

### Customize Prompts

Edit `config.py`:

```python
ROUTER_SYSTEM_PROMPT = """Your custom router prompt"""
SQL_GENERATOR_SYSTEM_PROMPT = """Your custom SQL prompt"""
RESPONSE_SYSTEM_PROMPT = """Your custom response prompt"""
```

## 🧪 Testing

### Run CLI Demo

```bash
# Interactive mode
python demo_cli.py

# Batch mode (runs predefined questions)
python demo_cli.py --batch
```

### Run Web UI

```bash
streamlit run streamlit_app_new.py
```

### Run Production Examples

```bash
# See all integration examples
python production_example.py
```

### Test in Python REPL

```python
python
>>> from chatbot_core import create_chatbot
>>> chatbot = create_chatbot()
>>> response = chatbot.ask("How many projects?")
>>> print(response['final_answer'])
```

## 📊 Response Format

The `chatbot.ask()` method returns a dictionary:

```python
{
    'final_answer': 'There are 5 real estate projects in the database.',
    'query_type': 'data',  # or 'general'
    'sql_query': 'SELECT COUNT(*) FROM projects',
    'error': ''  # Empty if no error
}
```

## 🔍 Troubleshooting

### Issue: "Invalid API key"

**Solution:** Check your `.env` file has `OPENROUTER_API_KEY` set correctly.

```bash
cat .env | grep OPENROUTER_API_KEY
```

### Issue: "Database not found"

**Solution:** The database will be created automatically on first run. If you see errors:

```python
from database import db_interface
db_interface.test_connection()
```

### Issue: "Module not found"

**Solution:** Install dependencies:

```bash
pip install -r requirements.txt
```

### Issue: Import errors between modules

**Solution:** Make sure you're in the project directory:

```bash
cd raisn_chatbot
python demo_cli.py
```

## 📚 Next Steps

1. **Read Architecture Guide**: See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed design
2. **Try Production Examples**: See [production_example.py](production_example.py)
3. **Customize Prompts**: Edit [config.py](config.py)
4. **Deploy to Production**: Choose your integration method from examples

## 🎓 Learning Path

### Beginner
1. Run `demo_cli.py` to understand basic usage
2. Read `chatbot_core.py` to see the workflow
3. Try simple Python integration example

### Intermediate
1. Run `streamlit_app_new.py` to see UI integration
2. Customize prompts in `config.py`
3. Try FastAPI integration example

### Advanced
1. Read `ARCHITECTURE.md` for full design
2. Implement custom integration
3. Deploy to production (Lambda, Docker, etc.)

## 💡 Key Concepts

### 1. Chatbot Workflow (LangGraph)
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

### 2. Stateless vs Stateful
- **Stateless**: Each query independent (`preserve_history=False`)
- **Stateful**: Queries use context (`preserve_history=True`, default)

### 3. Error Handling
- Automatic retry for failed SQL (up to 2 times)
- User-friendly error messages
- Graceful degradation

## 🚢 Deployment Checklist

- [ ] Set `OPENROUTER_API_KEY` in production environment
- [ ] Ensure database file is accessible
- [ ] Configure retry limits in `config.py`
- [ ] Add logging (optional but recommended)
- [ ] Add rate limiting (if exposed as API)
- [ ] Add authentication (if needed)
- [ ] Test error handling
- [ ] Monitor API costs

## 📞 Support

- **Architecture Questions**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Integration Examples**: See [production_example.py](production_example.py)
- **Code Issues**: Check inline documentation in modules

---

**You're ready to go!** Start with `python demo_cli.py` and integrate into your production app using the simple API: `chatbot.ask(question)`.
