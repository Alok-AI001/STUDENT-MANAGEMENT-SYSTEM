# Student Management System

A responsive web-based Student Management System built with Python, Flask and SQLAlchemy. This is the web version of the original console project; the original Python file is retained for reference.

## Features

- Add, view, search, update and delete student records
- Dashboard showing student count and average marks
- Responsive interface for desktop and mobile
- Validates required fields, age and marks
- Prevents duplicate student IDs
- SQLite for local development; PostgreSQL supported through `DATABASE_URL`

## Student fields

Student ID, name, age, course, branch and marks.

## Technology

Python 3 · Flask · Flask-SQLAlchemy · SQLAlchemy · SQLite/PostgreSQL · HTML · CSS · Jinja2

## Run locally (Windows PowerShell)

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
``

Open http://127.0.0.1:5000 in your browser.

## Deploy on Render

Create or open a **Web Service** connected to this repository's `main` branch and use:

| Setting | Value |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

Set the `SECRET_KEY` environment variable to a long random secret. For persistent student records, create a PostgreSQL database on Render and set `DATABASE_URL` to its **Internal Database URL** on the web service. The application automatically uses PostgreSQL when that variable is present; otherwise it uses a local SQLite file. The filesystem of a free Render web service is ephemeral, so SQLite data may be lost when the service is restarted or redeployed. Check Render's current database pricing and free-instance limits before creating a database.

After committing changes to `main`, Render can automatically deploy the latest commit if Auto-Deploy is enabled.

## Original console program

`student_manegement_system_mysql.py` is the original menu-driven Python version. Despite the filename, that original file used an in-memory Python list, not a MySQL connection.
