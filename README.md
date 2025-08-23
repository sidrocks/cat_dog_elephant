\# Flask Animal Selector + File Upload Demo



This is a simple \*\*Flask web app\*\* with an HTML/CSS/JS frontend.



\- \*\*Animal Selector\*\*: Choose Cat, Dog, or Elephant → the corresponding image is displayed.  

\- \*\*File Upload\*\*: Upload any file → the app shows its \*\*name, size, and type\*\*.  



---



\## 📁 Project Structure



flask\_app/

├── app.py

├── requirements.txt

├── .env # optional, for Flask settings

├── static/

│ ├── cat.jpg

│ ├── dog.jpg

│ └── elephant.jpg

└── templates/

└── index.html





---



\## 🚀 Setup Instructions (using uv)



1\. \*\*Create a virtual environment\*\*

&nbsp;  ```bash

&nbsp;  uv venv



2\. \*\*Activate it\*\*



Linux / macOS:



source .venv/bin/activate





Windows PowerShell:



.venv\\Scripts\\activate



3\. \*\*Install dependencies\*\*



uv pip sync requirements.txt



\*\*Running the App\*\*



\*\*Option 1: Using Flask CLI\*\*



Make sure .env exists:



FLASK\_APP=app

FLASK\_ENV=development

FLASK\_DEBUG=1





Run:



python -m flask run



\*\*Option 2: Run directly\*\*



app.py already has:



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   app.run(debug=True)





So you can also run:



python app.py



\*\*Usage\*\*



1\. Open browser at:

&nbsp;  http://127.0.0.1:5000



2\. \*\*Animal Box:\*\* Select Cat / Dog / Elephant → the corresponding image is displayed.



3\. \*\*File Upload Box:\*\* Upload a file → the app shows file details:



&nbsp;	-Name

&nbsp;	-Size (bytes)

&nbsp;	-Type (MIME type)Usage



 \*\*Dependencies\*\*



Flask

python-dotenv

werkzeug

click

itsdangerous

jinja2



(All installed automatically via requirements.txt)

