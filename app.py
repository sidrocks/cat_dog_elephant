from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Gemini API
#GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_KEY = 'EnterGoogleAPIKey'
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    file_info = {
        "name": file.filename,
        "size": os.path.getsize(filepath),
        "type": file.content_type
    }

    return jsonify(file_info)


def get_gemini_response(message):
    """Get response from Gemini model"""
    if not model:
        return "Gemini API key not configured. Please set GEMINI_API_KEY environment variable."
    
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages with Gemini"""
    data = request.get_json()
    message = data.get('message', '')
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_gemini_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
