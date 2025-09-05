# Flask AI Assistant - Complete Setup Guide

## 🚀 Quick Start (Recommended)

### Step 1: Install Dependencies
```bash
pip install flask google-generativeai python-dotenv
```

### Step 2: Get Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### Step 3: Configure Environment
Create a `.env` file in your project root:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the App
Open your browser and go to: `http://localhost:5000`

---

## 🛠️ Detailed Setup Options

### Option A: Using pip (Simple)
```bash
# Install dependencies
pip install flask google-generativeai python-dotenv

# Run the app
python app.py
```

### Option B: Using uv (Advanced)
```bash
# Create virtual environment
uv venv

# Activate environment
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\activate

# Install dependencies
uv pip sync requirements.txt

# Run the app
python app.py
```

### Option C: Using Flask CLI
```bash
# Create .env file with:
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
GEMINI_API_KEY=your_api_key_here

# Run with Flask CLI
python -m flask run
```

---

## 🎯 Features Overview

### 🤖 AI Conversation Agent
- **Model**: Gemini 2.5 Flash
- **Capabilities**: Natural language processing, creative writing, code generation
- **Formatting**: Markdown support with rich text rendering
- **Links**: Automatic URL detection and clickable links

### 🐾 Animal Integration
- **Selection**: Cat, Dog, or Elephant
- **AI Enhancement**: When an animal is selected, AI responses include:
  - Animal-themed contextual content
  - Funny poems about the selected animal
  - Enhanced prompts for animal-related responses
- **Visual**: Animal images displayed when selected

### 📁 File Upload System
- **Supported**: Any file type
- **Information**: Displays name, size, and MIME type
- **Storage**: Files saved to `uploads/` directory
- **Security**: Safe file handling and processing

### 🎨 User Interface
- **Design**: Modern, responsive layout
- **Layout**: Side-by-side panels (features on left, chat on right)
- **Styling**: Gradient backgrounds, smooth animations
- **Responsive**: Works on desktop and mobile devices

---

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main application page |
| `POST` | `/upload` | File upload endpoint |
| `POST` | `/chat` | AI chat endpoint |

### Chat Endpoint Details
```json
POST /chat
Content-Type: application/json

{
  "message": "Your message here"
}
```

Response:
```json
{
  "response": "AI response with markdown formatting"
}
```

---

## 🐛 Troubleshooting Guide

### Common Issues and Solutions

#### 1. Module Import Errors
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install flask google-generativeai python-dotenv
```

#### 2. API Key Issues
**Error**: "Gemini API key not configured"

**Solutions**:
- Ensure `.env` file exists in project root
- Verify API key format: `GEMINI_API_KEY=your_key_here`
- Check API key is valid at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Restart the application after adding the API key

#### 3. Chat Not Responding
**Possible Causes**:
- Internet connection issues
- Invalid API key
- Gemini API service issues

**Solutions**:
- Check internet connection
- Verify API key is working
- Check browser console for JavaScript errors
- Try a simple test message

#### 4. File Upload Issues
**Error**: File upload not working

**Solutions**:
- Ensure `uploads/` directory exists
- Check file permissions
- Verify file size limits
- Check browser console for errors

#### 5. Port Already in Use
**Error**: `Address already in use`

**Solutions**:
- Kill existing process: `Ctrl+C` in terminal
- Use different port: Modify `app.run(port=5001)` in `app.py`
- Find and kill process using port 5000

---

## 🔒 Security Considerations

### API Key Protection
- Never commit API keys to version control
- Use `.env` files for local development
- Use environment variables in production
- Regularly rotate API keys

### File Upload Security
- Files are stored in `uploads/` directory
- No file type restrictions (can be enhanced)
- Consider adding file size limits
- Implement virus scanning for production use

### XSS Prevention
- HTML is properly escaped in chat messages
- Only safe markdown elements are rendered
- Links open with `noopener noreferrer` for security

---

## 📊 Performance Tips

### For Development
- Use `debug=True` for auto-reload
- Enable Flask debug toolbar for performance monitoring
- Use browser dev tools to monitor network requests

### For Production
- Set `debug=False`
- Use a production WSGI server (Gunicorn, uWSGI)
- Implement proper logging
- Add rate limiting for API endpoints
- Use environment variables for configuration

---

## 🧪 Testing the Setup

### 1. Basic Functionality Test
1. Open `http://localhost:5000`
2. Verify all three sections are visible:
   - Animal Selector (left panel)
   - File Upload (left panel)
   - AI Chat (right panel)

### 2. Chat Test
1. Type "Hello" in the chat input
2. Press Enter or click Send
3. Verify AI responds with a greeting

### 3. Animal Integration Test
1. Select "Cat" from animal selector
2. Type "Tell me about programming"
3. Verify response includes cat-themed content and a cat poem

### 4. File Upload Test
1. Select any file using the file input
2. Click Upload
3. Verify file details are displayed

### 5. Markdown Test
1. Ask AI to "Write a list with headers and bold text"
2. Verify markdown formatting is rendered correctly

---

## 📝 Environment Variables

Create a `.env` file with these variables:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional (for Flask CLI)
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
```

---

## 🔄 Updates and Maintenance

### Updating Dependencies
```bash
pip install --upgrade flask google-generativeai python-dotenv
```

### Checking for Updates
- Monitor [Flask releases](https://pypi.org/project/Flask/)
- Check [Google AI updates](https://ai.google.dev/)
- Review security advisories

### Backup Recommendations
- Backup your `.env` file (without committing to git)
- Backup uploaded files in `uploads/` directory
- Document any custom modifications

---

## 📞 Support

### Getting Help
1. Check this setup guide first
2. Review the troubleshooting section
3. Check browser console for JavaScript errors
4. Verify all dependencies are installed correctly

### Common Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Google AI Documentation](https://ai.google.dev/docs)
- [Python Environment Setup](https://docs.python.org/3/tutorial/venv.html)
