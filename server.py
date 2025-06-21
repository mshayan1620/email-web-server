from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS emails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT NOT NULL,
                    recipient TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    body TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("SELECT * FROM emails ORDER BY timestamp DESC")
    emails = c.fetchall()
    conn.close()
    return render_template('index.html', emails=emails)

@app.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']
        conn = sqlite3.connect('emails.db')
        c = conn.cursor()
        c.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)",
                  (sender, recipient, subject, body))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('compose.html')

@app.route('/delete/<int:email_id>')
def delete_email(email_id):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("DELETE FROM emails WHERE id = ?", (email_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)