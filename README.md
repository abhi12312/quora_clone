# Quora Clone
A Django-based web application inspired by Quora, built with class-based views. Users can register, log in, post questions, view and answer questions, like answers, and log out.


## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python3
- Git
- Virtualenv: Install with: `pip install virtualenv`.


## Setup Steps

Follow these steps:

1. **Clone the Repository**:
    ```bash
   git clone https://github.com/your-username/quora_clone.git
   cd quora_clone

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
    ```bash
    pip install django

3. **Apply Database Migrations**:
    ```bash

    python manage.py migrate

4. **Run the Development Server:**:
    ```bash

    python manage.py runserver   


The application will be available at http://127.0.0.1:8000/.


Access the Application:
Open your browser and navigate to http://127.0.0.1:8000/.

**how to use**

Register: /register/

Login: /login/

Ask Question: /questions/ask/

Answer a Question: /questions/<id>/

Like an Answer: Click "Like"

Logout: /logout/