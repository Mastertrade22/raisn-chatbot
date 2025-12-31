# GitHub Repository Setup Instructions

## Option 1: Create Repository on GitHub Website (Easiest)

### Step 1: Create the Repository

1. Go to: https://github.com/new
2. Fill in:
   - **Owner**: Mastertrade22
   - **Repository name**: `raisn-chatbot`
   - **Description**: "Real Estate AI Chatbot with LangGraph, Qwen, and DeepSeek"
   - **Visibility**: ✅ **Public** (required for free Streamlit hosting)
   - **DO NOT check**: "Add a README file"
   - **DO NOT check**: "Add .gitignore"
   - **DO NOT check**: "Choose a license"
3. Click "Create repository"

### Step 2: Push Your Code

After creating the repository, GitHub will show you commands. Or use these:

```bash
cd /Users/mudit/Documents/raisn_chatbot

# Add the GitHub repository as remote
git remote add origin https://github.com/Mastertrade22/raisn-chatbot.git

# Push the code
git branch -M main
git push -u origin main
```

**Note**: You may need to enter your GitHub credentials:
- Username: `Mastertrade22`
- Password: Use a Personal Access Token from https://github.com/settings/tokens

---

## Option 2: Using GitHub CLI (If you have it installed)

```bash
cd /Users/mudit/Documents/raisn_chatbot

# Create repository and push in one command
gh repo create raisn-chatbot --public --source=. --remote=origin --push
```

---

## After Pushing to GitHub

Your repository will be at: https://github.com/Mastertrade22/raisn-chatbot

Then proceed to **DEPLOYMENT_GUIDE.md** for deploying to Streamlit Cloud!

---

## Files That Will Be Uploaded

✅ All Python files (app.py, streamlit_app.py, etc.)
✅ Database file (real_estate_data.db)
✅ Requirements.txt
✅ Configuration files (.streamlit/config.toml)
❌ .env file (excluded by .gitignore - good for security!)
❌ Secrets (.streamlit/secrets.toml - you'll add this on Streamlit Cloud)

---

## Verify Your Upload

After pushing, visit: https://github.com/Mastertrade22/raisn-chatbot

You should see all your files there!
