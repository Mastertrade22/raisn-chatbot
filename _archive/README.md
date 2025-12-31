# Archive Directory

This directory contains old/legacy files that have been superseded by the new modular architecture.

**These files are kept for reference only.**

## Directory Structure

### legacy_code/
Legacy monolithic code that has been refactored:
- `app.py` - Original monolithic script → Superseded by `chatbot_core.py`
- `streamlit_app.py` - Old Streamlit UI → Superseded by `streamlit_app_new.py`

### import_scripts/
One-time database import scripts (no longer needed):
- `explore_purva.py`
- `full_excel_import.py`
- `import_from_excel.py`
- `import_purva.py`
- `import_purva_v2.py`
- `insert_casagrand_projects.py`
- `inspect_purva_sheet.py`

### old_tests/
Old test scripts superseded by new test suite:
- `test_db.py` → Superseded by `test_refactored.py`
- `verify_code.py`

### old_docs/
Old documentation superseded by new documentation:
- `README.md` → Superseded by `README_NEW.md`
- `QUICKSTART.md` → Superseded by `QUICKSTART_NEW.md`
- `DATABASE_SCHEMA.md` → Schema now in `database.py`
- `DEPLOYMENT_GUIDE.md`
- `STATUS_REPORT.md`
- `STREAMLIT_DEPLOYMENT.md`
- `SYSTEM_PROMPTS.md` → Prompts now in `config.py`
- `GITHUB_SETUP.md`

### misc/
Miscellaneous files:
- `Document`
- `Document.pub`
- `CLEANUP_PLAN.md`

## Can I Delete This Directory?

Yes, you can safely delete this entire `_archive/` directory if you're confident you don't need these old files for reference.

The current codebase is fully functional without any of these archived files.

## Archived on

December 31, 2025
