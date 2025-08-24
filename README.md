# Flask Animal Selector + File Upload Demo

This is a simple **Flask web app** with an HTML/CSS/JS frontend.

- **Animal Selector**: Choose Cat, Dog, or Elephant → the corresponding image is displayed.  
- **File Upload**: Upload any file → the app shows its **name, size, and type**.  

---

## 📁 Project Structure

flask_app/<br>
├── app.py<br>
├── requirements.txt<br>
├── .env # optional, for Flask settings<br>
├── static/<br>
│ ├── cat.jpg<br>
│ ├── dog.jpg<br>
│ └── elephant.jpg<br>
└── templates/<br>
└── index.html<br>

---

## 🚀 Setup Instructions (using uv)

1. **Create a virtual environment**
   ```bash
   uv venv

2. **Activate it**

    **Linux / macOS:**    
    source .venv/bin/activate
    
    **Windows PowerShell:**    
    .venv\Scripts\activate

3. **Install dependencies**

    uv pip sync requirements.txt

# ▶️ Running the App

**Option 1: Using Flask CLI**

Make sure .env exists:
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=1

Run:
python -m flask run

**Option 2: Run directly**

app.py already has:
if __name__ == "__main__":
    app.run(debug=True)

So you can also run:
python app.py

# 🌐 Usage

1. Open browser at:
   http://127.0.0.1:5000
2. **Animal Box:** Select Cat / Dog / Elephant → the corresponding image is displayed.
3. **File Upload Box:** Upload a file → the app shows file details:
  -Name
  -Size (bytes)
  -Type (MIME type)

