# Global Excellence Scholarship Portal

A web-based scholarship application system built with **Django**. This project allows students to view scholarship details and submit applications via a responsive web interface.

## 📋 Features
* **Homepage:** Landing page with program details and eligibility criteria.
* **Application System:** Functional form for submitting student data (Name, Email, GPA, Statement).
* **Modular Design:** Uses Django template inheritance (Base, Navbar, Footer) for consistent layout.
* **Responsive UI:** Academic-themed design ("Navy Blue & Gold") that works on mobile and desktop.

## 🛠 Prerequisites
Before running this project, ensure you have the following installed:
* **Python** (3.8 or higher)
* **pip** (Python package installer)

## 🚀 How to Run the Project

Follow these steps to set up and run the application on your local machine.

### 1. Clone or Download the Project
Navigate to the project directory in your terminal:
```bash
cd ANDB_project
2. Create and Activate Virtual Environment
It is recommended to run Django inside a virtual environment to manage dependencies.

Windows:

Bash

python -m venv .venv
.venv\Scripts\activate
Mac/Linux:

Bash

python3 -m venv .venv
source .venv/bin/activate
(You should see (.venv) appear at the start of your command line line).

3. Install Dependencies
Install Django and any other required packages:

Bash

pip install django
4. Apply Database Migrations
Initialize the SQLite database:

Bash

python manage.py migrate
5. Run the Development Server
Start the server:

Bash

python manage.py runserver
6. Access the Application
Open your web browser and go to:

Homepage: http://127.0.0.1:8000/

Apply Page: http://127.0.0.1:8000/apply/

📂 Project Structure
Plaintext

ANDB_project/
├── db.sqlite3            # Database file (created after migrate)
├── manage.py             # Django command-line utility
├── scholarship/          # Main project configuration (settings, urls)
├── main/                 # The App containing views and logic
│   ├── views.py          # Handles page logic (homepage, apply)
│   ├── models.py         # Database models
│   └── ...
└── templates/            # HTML files
    ├── base.html         # Main skeleton (CSS + Structure)
    ├── homepage.html     # Home content
    ├── apply.html        # Application form
    └── parts/            # Reusable components
        ├── navbar.html
        └── footer.html
