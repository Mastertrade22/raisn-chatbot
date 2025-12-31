# Cleanup Plan

## Files to KEEP (Production & Essential)

### Core Modules ✅
- `chatbot_core.py` - Main chatbot
- `config.py` - Configuration
- `database.py` - Database interface
- `llm_client.py` - LLM client
- `real_estate_db.py` - Database setup
- `real_estate_data.db` - SQLite database

### Demo/Frontend ✅
- `demo_cli.py` - CLI demo
- `streamlit_app_new.py` - Modern Streamlit UI
- `production_example.py` - Integration examples
- `test_refactored.py` - Test suite

### Documentation ✅
- `README_NEW.md` - Main documentation
- `QUICKSTART_NEW.md` - Quick start guide
- `ARCHITECTURE.md` - Architecture documentation
- `REFACTORING_SUMMARY.md` - Refactoring summary

### Configuration ✅
- `requirements.txt` - Dependencies
- `.env` - Environment variables
- `.gitignore` - Git ignore rules

### Git/IDE ✅
- `.git/` - Git repository
- `.devcontainer/` - Dev container config
- `.streamlit/` - Streamlit config
- `__pycache__/` - Python cache (auto-generated)

---

## Files to REMOVE or ARCHIVE

### Legacy Code (Superseded by new modules)
- `app.py` - Old monolithic script (superseded by chatbot_core.py)
- `streamlit_app.py` - Old Streamlit UI (superseded by streamlit_app_new.py)

### Database Import Scripts (One-time use)
- `explore_purva.py` - Data exploration script
- `full_excel_import.py` - Excel import script
- `import_from_excel.py` - Excel import script
- `import_purva.py` - Purva data import
- `import_purva_v2.py` - Purva data import v2
- `insert_casagrand_projects.py` - Casagrand data import
- `inspect_purva_sheet.py` - Sheet inspection script

### Old Test/Verification Scripts
- `test_db.py` - Old database test (superseded by test_refactored.py)
- `verify_code.py` - Old verification script

### Old Documentation (Superseded)
- `README.md` - Old README (superseded by README_NEW.md)
- `QUICKSTART.md` - Old quickstart (superseded by QUICKSTART_NEW.md)
- `DATABASE_SCHEMA.md` - Redundant (schema in database.py)
- `DEPLOYMENT_GUIDE.md` - Outdated deployment guide
- `GITHUB_SETUP.md` - GitHub setup (may keep if needed)
- `STATUS_REPORT.md` - Old status report
- `STREAMLIT_DEPLOYMENT.md` - Old Streamlit guide
- `SYSTEM_PROMPTS.md` - Redundant (prompts in config.py)

### Mysterious Files
- `Document` - Unknown file
- `Document.pub` - Unknown public key file

---

## Recommendation

### Option 1: Archive Old Files (Safer)
Move old files to `_archive/` directory for reference

### Option 2: Delete Old Files (Cleaner)
Remove files that are truly not needed

I recommend **Option 1** (archive) to be safe.
