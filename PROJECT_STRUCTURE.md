# Project Structure

## 📁 Current Directory Structure

```
raisn_chatbot/
├── Core Modules (Production-Ready)
│   ├── chatbot_core.py          # Main chatbot logic
│   ├── config.py                # Configuration & prompts
│   ├── database.py              # Database interface
│   ├── llm_client.py            # LLM API client
│   └── real_estate_db.py        # Database setup
│
├── Demo/Frontend
│   ├── demo_cli.py              # Interactive CLI demo
│   ├── streamlit_app_new.py    # Modern Streamlit UI
│   ├── production_example.py    # Integration examples
│   └── test_refactored.py       # Test suite
│
├── Documentation
│   ├── README_NEW.md            # Main documentation
│   ├── QUICKSTART_NEW.md        # Quick start guide
│   ├── ARCHITECTURE.md          # Architecture details
│   ├── REFACTORING_SUMMARY.md   # Refactoring summary
│   └── PROJECT_STRUCTURE.md     # This file
│
├── Data
│   └── real_estate_data.db     # SQLite database
│
├── Configuration
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables
│   ├── .gitignore              # Git ignore rules
│   ├── .streamlit/             # Streamlit config
│   └── .devcontainer/          # Dev container config
│
└── Archive
    └── _archive/                # Old/legacy files (safe to delete)
        ├── legacy_code/         # app.py, streamlit_app.py
        ├── import_scripts/      # One-time import scripts
        ├── old_tests/          # Old test scripts
        ├── old_docs/           # Old documentation
        └── misc/               # Miscellaneous files
```

## 🎯 File Purpose Guide

### Core Production Files

| File | Purpose | Use In Production? |
|------|---------|-------------------|
| `chatbot_core.py` | Main chatbot with LangGraph workflow | ✅ YES |
| `config.py` | All configurations, prompts, settings | ✅ YES |
| `database.py` | Database interface and operations | ✅ YES |
| `llm_client.py` | LLM API client with error handling | ✅ YES |
| `real_estate_db.py` | Database setup and schema | ✅ YES |
| `real_estate_data.db` | SQLite database file | ✅ YES |

### Demo/Testing Files

| File | Purpose | Use In Production? |
|------|---------|-------------------|
| `demo_cli.py` | Interactive CLI for testing | ❌ NO (demo) |
| `streamlit_app_new.py` | Web UI for demo | ❌ NO (frontend) |
| `production_example.py` | Integration examples | ❌ NO (examples) |
| `test_refactored.py` | Test suite | ❌ NO (testing) |

### Documentation Files

| File | Purpose |
|------|---------|
| `README_NEW.md` | Main project documentation |
| `QUICKSTART_NEW.md` | Getting started guide |
| `ARCHITECTURE.md` | Architecture documentation |
| `REFACTORING_SUMMARY.md` | Before/after comparison |
| `PROJECT_STRUCTURE.md` | This file - directory structure |

### Configuration Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Python package dependencies |
| `.env` | Environment variables (API keys) |
| `.gitignore` | Files to ignore in git |

## 🗑️ Archived Files

All old/legacy files have been moved to `_archive/`:

- **Legacy code**: `app.py`, `streamlit_app.py`
- **Import scripts**: One-time database import scripts
- **Old tests**: Superseded test scripts
- **Old docs**: Superseded documentation

**You can safely delete the entire `_archive/` directory if you don't need these files for reference.**

## 📊 File Count Summary

| Category | Count |
|----------|-------|
| Core modules | 6 files |
| Demo/Frontend | 4 files |
| Documentation | 5 files |
| Configuration | 3 files |
| Total active files | 18 files |
| Archived files | 20+ files |

## 🚀 Quick Reference

### Run Tests
```bash
python test_refactored.py
```

### Run CLI Demo
```bash
python demo_cli.py
```

### Run Web UI
```bash
streamlit run streamlit_app_new.py
```

### Use in Production
```python
from chatbot_core import create_chatbot
chatbot = create_chatbot()
response = chatbot.ask("Your question")
```

## 🧹 Cleanup Summary

**Date:** December 31, 2025

**Actions Taken:**
- ✅ Created modular architecture
- ✅ Moved 20+ legacy files to `_archive/`
- ✅ Cleaned up directory structure
- ✅ Created comprehensive documentation
- ✅ All tests passing

**Result:** Clean, production-ready codebase with 70% fewer files in main directory.
