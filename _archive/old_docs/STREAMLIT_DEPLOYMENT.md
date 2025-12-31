# 🚀 Streamlit Cloud Deployment Guide

## Complete Step-by-Step Guide to Deploy Your Chatbot

---

## ✅ Prerequisites (Make Sure You've Done These)

- [x] GitHub repository created at: `https://github.com/Mastertrade22/raisn-chatbot`
- [x] Code pushed to GitHub (all files visible in the repository)
- [x] OpenRouter API key ready

---

## 🎯 Deployment Steps

### **Step 1: Go to Streamlit Cloud**

1. Open your browser and navigate to: **https://share.streamlit.io**
2. You'll see the Streamlit Cloud homepage

### **Step 2: Sign Up / Sign In**

1. Click the **"Sign in"** button (top right)
2. Click **"Continue with GitHub"**
3. A GitHub authorization page will open
4. Click **"Authorize streamlit"**
5. You'll be redirected back to Streamlit Cloud

### **Step 3: Create New App**

1. You should now see your Streamlit Cloud dashboard
2. Click the big **"New app"** button
3. You'll see a deployment form with three main sections

### **Step 4: Configure Your App**

Fill in the deployment form:

#### **Repository, branch, and file**

- **Repository**: Select or type `Mastertrade22/raisn-chatbot`
  - If you don't see it, click "Paste GitHub URL" and enter: `https://github.com/Mastertrade22/raisn-chatbot`
- **Branch**: `main`
- **Main file path**: `streamlit_app.py`

#### **App URL (Optional)**

- Streamlit will auto-generate a URL like: `raisn-chatbot.streamlit.app`
- You can customize it if you want (must be unique across all Streamlit apps)

### **Step 5: Advanced Settings (CRITICAL!)**

**This is the most important step - don't skip it!**

1. Click **"Advanced settings..."** at the bottom
2. A panel will expand with several options

#### **Python version**
- Select: `3.11` or `3.12` (recommended)

#### **Secrets** (MOST IMPORTANT!)

In the **Secrets** text area, paste:

```toml
OPENROUTER_API_KEY = "sk-or-v1-YOUR-ACTUAL-API-KEY-HERE"
```

**IMPORTANT**: Replace `sk-or-v1-YOUR-ACTUAL-API-KEY-HERE` with your real OpenRouter API key!

**Example** (with a fake key):
```toml
OPENROUTER_API_KEY = "sk-or-v1-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz"
```

**Note**:
- This keeps your API key secret and secure
- It won't be visible in your GitHub repository
- It's the same as having a `.env` file locally

### **Step 6: Deploy!**

1. Double-check everything:
   - ✅ Repository: `Mastertrade22/raisn-chatbot`
   - ✅ Branch: `main`
   - ✅ File: `streamlit_app.py`
   - ✅ API key added to secrets
2. Click the **"Deploy!"** button

### **Step 7: Wait for Deployment**

You'll see a build log with progress:

```
Creating your app...
Installing dependencies...
Running streamlit_app.py...
```

This takes **2-5 minutes**. You'll see:
- Installing Python packages from `requirements.txt`
- Creating the database
- Starting the Streamlit app

### **Step 8: Your App is Live! 🎉**

Once deployment completes:
- The build log will disappear
- Your app will load automatically
- You'll see the chat interface
- The URL will be: `https://[your-app-name].streamlit.app`

---

## 🧪 Testing Your Live App

### First Tests:

1. **Check API Key Status**:
   - Look at the sidebar
   - Should show: "✅ API Key Loaded"
   - If it shows "❌ No API Key Found", go back and add the secret

2. **Try Example Questions**:
   - Click any example question in the sidebar
   - For example: "How many projects are under construction?"

3. **Test Both Models**:
   - Select "Both (Comparison)" in the sidebar
   - Ask a question
   - You should see responses from both Qwen and DeepSeek

4. **Test Database Queries**:
   - Ask: "Show me all 3BHK units"
   - Click "🔍 View SQL Query" to see the generated SQL

---

## 🎨 Your App Features

Once live, users can:
- ✅ Chat with AI about real estate data
- ✅ Choose between Qwen 2.5 or DeepSeek V3
- ✅ Compare both models side-by-side
- ✅ View generated SQL queries
- ✅ Try example questions
- ✅ Clear chat history
- ✅ Access from mobile or desktop

---

## 🔧 Troubleshooting

### Problem 1: "❌ No API Key Found"

**Symptoms**: Sidebar shows API key not loaded

**Solution**:
1. Go to your Streamlit Cloud dashboard: https://share.streamlit.io
2. Click on your app
3. Click the menu (⋮) → "Settings"
4. Click "Secrets" on the left
5. Add or fix your API key:
   ```toml
   OPENROUTER_API_KEY = "your-actual-key"
   ```
6. Click "Save"
7. Click "Reboot app"

### Problem 2: "Module not found" Error

**Symptoms**: Error message about missing Python packages

**Solution**:
1. Check that `requirements.txt` has all dependencies
2. Make sure you pushed the latest `requirements.txt` to GitHub
3. Current requirements should be:
   ```
   langgraph>=0.0.20
   langchain>=0.1.0
   langchain-community>=0.0.20
   requests>=2.31.0
   python-dotenv>=1.0.0
   streamlit>=1.28.0
   ```
4. Reboot the app from Streamlit Cloud dashboard

### Problem 3: Database Errors

**Symptoms**: "Database not found" or SQLite errors

**Solution**:
1. Make sure `real_estate_data.db` was pushed to GitHub
2. Make sure `real_estate_db.py` is in the repository
3. The database should be created automatically on first run
4. Check the logs for specific SQLite errors

### Problem 4: App is Slow or Sleeping

**Symptoms**: Takes long to load on first visit

**Explanation**:
- Free tier apps "sleep" after inactivity
- First visit after sleep takes 30-60 seconds to wake up
- Subsequent visits are instant
- This is normal for free tier!

### Problem 5: Build Fails

**Symptoms**: Red error messages during deployment

**Solution**:
1. Click "Manage app" → "Logs" to see detailed error
2. Common fixes:
   - Check Python version (use 3.11 or 3.12)
   - Verify all files are in GitHub
   - Check for typos in file names
3. You can redeploy anytime from the dashboard

---

## 🔄 Updating Your App

Made changes to the code? Here's how to update:

### On Your Computer:

```bash
cd /Users/mudit/Documents/raisn_chatbot

# Make your changes to files...

# Commit changes
git add .
git commit -m "Description of changes"

# Push to GitHub
git push
```

### On Streamlit Cloud:

- **Automatic**: Streamlit detects GitHub changes and redeploys automatically (takes 1-2 minutes)
- **Manual**: Go to dashboard → Click menu (⋮) → "Reboot app"

---

## 📊 Managing Your App

### Streamlit Cloud Dashboard

Access at: https://share.streamlit.io

From here you can:
- **View logs**: See what's happening in your app
- **Reboot app**: Restart if something goes wrong
- **Delete app**: Remove the deployment
- **Settings**: Change secrets, Python version, etc.
- **Analytics**: See how many people are using your app

### Viewing Logs

1. Go to dashboard
2. Click your app
3. Click menu (⋮) → "Logs"
4. See real-time logs of:
   - User requests
   - API calls
   - Errors
   - Database queries

---

## 🌐 Sharing Your App

### Your Public URL:

```
https://[your-app-name].streamlit.app
```

### Share it anywhere:
- Send the link to friends/colleagues
- Share on social media
- Embed in your portfolio
- Add to your resume
- No login required for users!

### Custom Domain (Optional)

Free tier doesn't support custom domains, but the streamlit.app URL works great!

---

## 💰 Free Tier Limits

What you get for **FREE**:
- ✅ Unlimited public apps
- ✅ 1 GB storage per app
- ✅ Shared CPU/RAM resources
- ✅ Automatic HTTPS
- ✅ Automatic deployments from GitHub

Limitations:
- ⚠️ Apps sleep after inactivity (wake on visit)
- ⚠️ Shared resources (may be slower during peak times)
- ⚠️ Must be public repositories
- ⚠️ 1 GB storage limit

**For this chatbot**: Free tier is perfect! Your database is small and the app works great.

---

## 🎓 Next Steps

After successful deployment:

### Immediate:
1. ✅ Test all features
2. ✅ Share the URL
3. ✅ Get feedback from users

### Soon:
1. **Customize UI**: Edit `streamlit_app.py` for different colors, layout
2. **Add more data**: Expand your database
3. **Try more models**: OpenRouter has 100+ models
4. **Add features**:
   - Save chat history
   - Export conversations
   - Add images of properties
   - User feedback buttons

### Advanced:
1. **Analytics**: Track usage patterns
2. **Rate limiting**: Prevent API abuse
3. **User authentication**: Add login if needed
4. **Database sync**: Auto-update from Excel files

---

## 📚 Helpful Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Deployment Guide**: https://docs.streamlit.io/deploy/streamlit-community-cloud
- **Community Forum**: https://discuss.streamlit.io
- **OpenRouter Docs**: https://openrouter.ai/docs
- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/

---

## 🆘 Need Help?

If you get stuck:

1. **Check the logs** in Streamlit Cloud dashboard
2. **Search the error** on Streamlit Community forum
3. **Test locally** first with `streamlit run streamlit_app.py`
4. **Check GitHub** - make sure all files are pushed
5. **Verify API key** - most issues are from missing/wrong API key

---

## ✨ You're Ready!

Follow the steps above and your chatbot will be live on the internet in **under 10 minutes**!

**Start at Step 1** and work your way through. Good luck! 🚀
