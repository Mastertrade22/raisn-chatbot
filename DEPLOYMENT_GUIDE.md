# 🚀 Deployment Guide - Real Estate AI Chatbot

## Quick Start: Deploy to Streamlit Cloud (FREE)

Follow these steps to deploy your chatbot to the web for free!

---

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name**: `raisn-chatbot` (or any name you prefer)
   - **Description**: "Real Estate AI Chatbot with LangGraph and Streamlit"
   - **Visibility**: Public (required for free Streamlit hosting)
   - **DO NOT** initialize with README (we already have files)
3. Click "Create repository"

---

## Step 2: Push Your Code to GitHub

Copy and run these commands in your terminal:

```bash
cd /Users/mudit/Documents/raisn_chatbot

# Add the GitHub repository as remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/Mastertrade22/raisn-chatbot.git

# Push the code
git branch -M main
git push -u origin main
```

If prompted for credentials:
- Username: Your GitHub username
- Password: Use a [Personal Access Token](https://github.com/settings/tokens) (not your GitHub password)

---

## Step 3: Deploy to Streamlit Cloud

### 3.1 Sign Up for Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "Continue with GitHub"
3. Authorize Streamlit to access your GitHub account

### 3.2 Create New App

1. Click the "New app" button
2. Fill in the deployment form:
   - **Repository**: `Mastertrade22/raisn-chatbot`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
3. Click "Advanced settings" (IMPORTANT!)

### 3.3 Add Your API Key (CRITICAL STEP!)

In the Advanced settings, find the "Secrets" section and add:

```toml
OPENROUTER_API_KEY = "sk-or-v1-YOUR-ACTUAL-API-KEY-HERE"
```

Replace `sk-or-v1-YOUR-ACTUAL-API-KEY-HERE` with your real OpenRouter API key.

### 3.4 Deploy!

1. Click "Deploy!"
2. Wait 2-5 minutes for the app to build
3. Your app will be live at: `https://your-app-name.streamlit.app`

---

## Step 4: Test Your Live App

Once deployed:
1. The app will automatically create the database on first run
2. Try asking: "How many projects are under construction?"
3. Test different AI models (Qwen vs DeepSeek)
4. Share the URL with anyone!

---

## Troubleshooting

### Problem: "No API Key Found"

**Solution**:
- Go to Streamlit Cloud dashboard
- Click your app → Settings → Secrets
- Add your `OPENROUTER_API_KEY`
- Restart the app

### Problem: Import Errors

**Solution**:
- Check that all files were pushed to GitHub
- Verify `requirements.txt` has all dependencies
- View logs in Streamlit Cloud for specific errors

### Problem: Database Errors

**Solution**:
- The database should be created automatically
- Make sure `real_estate_data.db` is in your GitHub repo
- Check Streamlit Cloud logs for specific SQLite errors

---

## Testing Locally Before Deployment

Want to test locally first?

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "OPENROUTER_API_KEY=your-api-key-here" > .env

# Run Streamlit locally
streamlit run streamlit_app.py
```

Open http://localhost:8501 in your browser

---

## What You'll Get

- **Free hosting** on Streamlit Cloud
- **Public URL** to share with anyone
- **Automatic updates** when you push to GitHub
- **No server management** required
- **Mobile-friendly** interface

---

## Sharing Your App

Once live, share your URL:
```
https://your-app-name.streamlit.app
```

Anyone can access it without login!

---

## Free Tier Limits

Streamlit Community Cloud free tier:
- ✅ Unlimited public apps
- ✅ 1 GB storage per app
- ✅ Shared compute resources
- ⚠️ Apps may sleep after inactivity (wake instantly when accessed)

---

## Need Help?

- **Streamlit Docs**: https://docs.streamlit.io/deploy
- **Community Forum**: https://discuss.streamlit.io
- **OpenRouter**: https://openrouter.ai/docs

---

## Next Steps After Deployment

1. **Customize the UI** - Edit `streamlit_app.py`
2. **Add more data** - Update the database
3. **Try different models** - Explore OpenRouter's model catalog
4. **Share with users** - Get feedback on your chatbot!

---

**Ready to deploy? Start with Step 1 above! 🚀**
