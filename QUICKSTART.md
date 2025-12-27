# Quick Start Guide

Get your LangGraph Real Estate Chatbot running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai/keys))

## Step 1: Install Dependencies

```bash
cd raisn_chatbot
pip install -r requirements.txt
```

## Step 2: Configure API Key

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenRouter API key:

```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
```

## Step 3: Test the Database (Optional)

Verify the database setup:

```bash
python test_db.py
```

Expected output:
```
✅ Database created!
✓ Total projects: 4
✓ Total units: 10
✓ Cheapest 2BHK: Godrej Woodsville - ₹55,00,000
...
```

## Step 4: Run the Chatbot

```bash
python app.py
```

This will:
1. Create the real estate database with sample data
2. Run 8 test questions comparing Qwen 2.5 and DeepSeek V3 models
3. Display side-by-side results for each model

## What You'll See

```
🏗️ Setting up Real Estate database...
✅ Database ready!

======================================================================
QUESTION: How many projects are under construction?
======================================================================

──────────────────────────────────────────────────────────────────────
🤖 Testing with Qwen 2.5
──────────────────────────────────────────────────────────────────────

[qwen/qwen-2.5-72b-instruct] 🧭 Router analyzing question...
[qwen/qwen-2.5-72b-instruct] ✅ Classified as: data
[qwen/qwen-2.5-72b-instruct] 🔧 Generating SQL query...
[qwen/qwen-2.5-72b-instruct] 📝 Generated SQL: SELECT COUNT(*) FROM projects WHERE construction_status = 'Under Construction'
[qwen/qwen-2.5-72b-instruct] 🗄️  Executing SQL...
[qwen/qwen-2.5-72b-instruct] ✅ Query successful: 1 rows
[qwen/qwen-2.5-72b-instruct] 💬 Generating final response...
[qwen/qwen-2.5-72b-instruct] ✅ Response generated

✨ Qwen 2.5 Response:
There are 3 projects currently under construction.

──────────────────────────────────────────────────────────────────────
🤖 Testing with DeepSeek V3
──────────────────────────────────────────────────────────────────────
...
```

## Sample Questions Tested

1. "How many projects are under construction?"
2. "Which projects have more than 75% open space?"
3. "What is the cheapest 2BHK apartment available?"
4. "Show me all 3BHK units with their prices"
5. "Which units have festive offers right now?"
6. "What is the average price per sqft for villas?"
7. "List all projects by Prestige Group with their unit types"
8. "Show me projects near the airport with pricing details"

## Try Your Own Questions

Modify the `test_questions` list in [app.py](app.py#L535-L544):

```python
test_questions = [
    "Your custom question here",
    "Another question",
]
```

## Understanding the Output

For each question, you'll see:

### 1. Node Execution Logs
```
[model-name] 🧭 Router analyzing question...
[model-name] ✅ Classified as: data
[model-name] 🔧 Generating SQL query...
[model-name] 📝 Generated SQL: SELECT ...
[model-name] 🗄️  Executing SQL...
[model-name] ✅ Query successful: X rows
[model-name] 💬 Generating final response...
[model-name] ✅ Response generated
```

### 2. Model Response
```
✨ Qwen 2.5 Response:
There are 3 projects currently under construction.
```

### 3. Comparison Summary
```
📊 COMPARISON SUMMARY
======================================================================

Qwen 2.5: ✅ Success
  Query Type: data
  SQL: SELECT COUNT(*) FROM projects WHERE construction_status = 'Under Construction'
  Answer: There are 3 projects currently under construction.

DeepSeek V3: ✅ Success
  Query Type: data
  SQL: SELECT COUNT(*) FROM projects WHERE construction_status = 'Under Construction'
  Answer: Currently, there are 3 projects under construction.
```

## Error Handling Examples

The chatbot gracefully handles errors:

### SQL Error with Retry
```
[model-name] ❌ SQL Error (attempt 1): no such column: invalid_column
[model-name] 🔧 Generating SQL query... (retry)
[model-name] 📝 Generated SQL: SELECT ... (corrected)
```

### User-Friendly Error Messages
```
✨ Response:
I apologize, but I'm having trouble processing your data query at the moment.
Please try rephrasing your question or try again in a moment.
```

## Next Steps

### Customize the Database

Edit [real_estate_db.py](real_estate_db.py) to:
- Add more projects
- Add more unit types
- Modify the schema
- Add your own data

### Customize System Prompts

Edit prompts in [app.py](app.py#L39-L104) to:
- Change classification rules
- Modify SQL generation behavior
- Adjust response tone

See [SYSTEM_PROMPTS.md](SYSTEM_PROMPTS.md) for detailed documentation.

### Add More Models

Edit the `models` dictionary in [app.py](app.py#L503-L506):

```python
models = {
    "Qwen 2.5": "qwen/qwen-2.5-72b-instruct",
    "DeepSeek V3": "deepseek/deepseek-chat",
    "GPT-4": "openai/gpt-4-turbo",  # Add more models
    "Claude": "anthropic/claude-3-opus"
}
```

## Troubleshooting

### "Invalid API key" Error
- Check your `.env` file
- Verify your OpenRouter API key at https://openrouter.ai/keys
- Make sure there are no extra spaces in the key

### "Database locked" Error
- Close any other programs accessing the database
- Delete `real_estate_data.db` and run again

### "Module not found" Error
```bash
pip install -r requirements.txt
```

### Models Not Responding
- Check your internet connection
- Verify OpenRouter service status
- Try increasing the timeout in [app.py](app.py#L142)

## Performance Tips

1. **Reduce test questions** for faster testing:
   ```python
   test_questions = test_questions[:2]  # Only test first 2 questions
   ```

2. **Test one model at a time**:
   ```python
   models = {"Qwen 2.5": "qwen/qwen-2.5-72b-instruct"}  # Comment out DeepSeek
   ```

3. **Use faster models** for testing:
   ```python
   models = {"GPT-3.5": "openai/gpt-3.5-turbo"}  # Faster & cheaper
   ```

## Learn More

- [README.md](README.md) - Complete documentation
- [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) - Database structure
- [SYSTEM_PROMPTS.md](SYSTEM_PROMPTS.md) - Prompt engineering guide
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) - Official LangGraph docs

## Support

Found an issue? Have a question?
- Check [SYSTEM_PROMPTS.md](SYSTEM_PROMPTS.md) for common customizations
- Review [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) for query examples
- Inspect the logs for detailed error information

Happy building! 🚀
