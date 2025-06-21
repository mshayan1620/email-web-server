# Email Web Server - v2

A basic email web server built with Python, Flask, SQLite, HTML, and CSS.

## Features
- Compose and send emails (saved in SQLite DB)
- Inbox page with list of emails
- Delete individual emails
- Navigation bar (Inbox / Compose)
- Web-based UI with HTML & CSS

## Technologies Used
- Python (Backend with Flask)
- SQLite (Database)
- HTML/CSS (Frontend)
- Jinja2 (Template engine for Flask)

## Purpose
Learn Flask + SQL + full-stack concepts in Python.

## How to Run

```bash
# 1. Go to project folder
cd email-web-server-v2

# 2. Create venv
python3 -m venv venv

# 3. Activate venv
source venv/bin/activate

# 4. Install Flask
python3 -m pip install Flask

# 5. Run app
python3 server.py
```

Visit: http://localhost:5000