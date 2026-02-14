from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "techinnovation"

ADMIN_PASS = "admin123"
EMP_PASS = "emp123"

def init_db():
    conn = sqlite3.connect('posts.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 message TEXT,
                 date TEXT)''')
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('posts.db')
    posts = conn.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    conn.close()
    role = session.get('role')
    return render_template('updates.html', posts=posts, role=role)

@app.route('/login', methods=['POST'])
def login():
    role = request.form['role']
    password = request.form['password']

    if role == "admin" and password == ADMIN_PASS:
        session['role'] = "admin"
    elif role == "employee" and password == EMP_PASS:
        session['role'] = "employee"

    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('role', None)
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    if session.get('role') in ["admin","employee"]:
        name = request.form['name']
        message = request.form['message']
        date = datetime.now().strftime("%d-%m-%Y")

        conn = sqlite3.connect('posts.db')
        conn.execute("INSERT INTO posts (name,message,date) VALUES (?,?,?)",
                     (name, message, date))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if session.get('role') == "admin":
        conn = sqlite3.connect('posts.db')
        conn.execute("DELETE FROM posts WHERE id=?", (id,))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
