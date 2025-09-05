# Flask AI Assistant with Animal Integration

A modern **Flask web application** featuring an AI-powered conversation agent integrated with Gemini 2.5 Flash, animal selector, and file upload functionality.

## ✨ Features

### 🤖 AI Conversation Agent
- **Gemini 2.5 Flash Integration**: Chat with Google's advanced AI model
- **Markdown Support**: Rich text formatting with headers, bold, italic, code blocks, and lists
- **Clickable Links**: Automatic URL detection and conversion to clickable links
- **Real-time Chat**: Modern chat interface with typing indicators
- **Animal Context Integration**: AI responses are themed around selected animals

### 🐾 Animal Selector
- **Interactive Selection**: Choose between Cat, Dog, or Elephant
- **Visual Display**: Shows corresponding animal images
- **AI Integration**: When an animal is selected, AI responses include:
  - Contextual animal-themed content
  - Funny poems about the selected animal
  - Enhanced prompts for animal-related responses

### 📁 File Upload
- **Drag & Drop Support**: Easy file upload interface
- **File Information**: Displays name, size, and MIME type
- **Secure Handling**: Safe file processing and storage

### 🎨 Modern UI/UX
- **Responsive Design**: Works on desktop and mobile devices
- **Gradient Styling**: Beautiful color schemes and animations
- **Side-by-Side Layout**: Organized interface with left and right panels
- **Real-time Updates**: Dynamic content updates without page refresh

---

## 📁 Project Structure

```
flask_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── SETUP.md              # Detailed setup instructions
├── static/               # Static assets
│   ├── cat.jpg
│   ├── dog.jpg
│   └── elephant.jpg
├── templates/            # HTML templates
│   └── index.html        # Main application page
└── uploads/              # File upload directory
```

---

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install flask google-generativeai python-dotenv
```

### 2. Configure Gemini API
- Get your API key from: https://makersuite.google.com/app/apikey
- Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Application
```bash
python app.py
```

### 4. Access the App
Open `http://localhost:5000` in your browser

---

## 🌐 Usage Guide

### Chat Interface
1. **Type your message** in the chat input field
2. **Press Enter** or click "Send" to send your message
3. **View AI responses** with rich markdown formatting
4. **Click links** to open them in new tabs

### Animal Integration
1. **Select an animal** (Cat, Dog, or Elephant) from the left panel
2. **Send any message** in the chat
3. **AI will respond** with:
   - Your original answer
   - Animal-themed contextual content
   - A funny poem about the selected animal
4. **Unselect the animal** to stop getting animal-themed responses

### File Upload
1. **Click "Choose File"** or drag a file to the upload area
2. **Click "Upload"** to process the file
3. **View file details** including name, size, and type

---

## 🔧 API Endpoints

- `GET /` - Main application page
- `POST /upload` - File upload endpoint
- `POST /chat` - AI chat endpoint with Gemini integration

---

## 🛠️ Advanced Setup (using uv)

### 1. Create Virtual Environment
```bash
uv venv
```

### 2. Activate Environment
**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows PowerShell:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
uv pip sync requirements.txt
```

### 4. Run with Flask CLI
Create `.env` file:
```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1
GEMINI_API_KEY=your_api_key_here
```

Run:
```bash
python -m flask run
```

---

## 🐛 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'flask'"**
```bash
pip install flask google-generativeai python-dotenv
```

**"API key not configured"**
- Ensure your `.env` file contains: `GEMINI_API_KEY=your_actual_key`
- Verify the API key is valid at https://makersuite.google.com/app/apikey

**Chat not responding**
- Check your internet connection
- Verify the Gemini API key is working
- Check browser console for JavaScript errors

**File upload not working**
- Ensure the `uploads/` directory exists
- Check file permissions
- Verify file size limits

---

## 🎯 Features in Detail

### Markdown Support
The AI responses support rich formatting:
- **Headers**: `# H1`, `## H2`, `### H3`
- **Bold**: `**text**` or `__text__`
- **Italic**: `*text*` or `_text_`
- **Code**: `` `inline code` `` and ``` code blocks ```
- **Lists**: `* item` or `1. item`
- **Links**: Automatic URL detection and conversion

### Animal Context Integration
When an animal is selected:
- AI responses are themed around the selected animal
- Includes funny poems about the animal
- Provides contextual animal-related information
- Maintains conversation flow while adding animal theme

### Security Features
- HTML escaping to prevent XSS attacks
- Secure file upload handling
- API key protection through environment variables
- Safe link opening with `noopener noreferrer`

---

## 📝 Example Usage

1. **Basic Chat**: Ask "What's the weather like?" → Get weather information
2. **Animal Chat**: Select "cat" + ask "Tell me about programming" → Get programming info with cat-themed context and a cat poem
3. **File Upload**: Upload a document → See file details displayed
4. **Rich Content**: AI responses with markdown formatting, clickable links, and structured content

---

## 🔮 Future Enhancements

- [ ] Image upload and analysis with Gemini Vision
- [ ] Chat history persistence
- [ ] Multiple AI model support
- [ ] Custom animal themes and poems
- [ ] Voice input/output integration
- [ ] Multi-language support

