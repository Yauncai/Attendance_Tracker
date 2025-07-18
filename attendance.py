import sqlite3
from flask import Flask, render_template, request, Response
from datetime import datetime

app = Flask(__name__)

DB = 'yaf_attendance.db'

# --- Database helper ---
def insert_attendance(name, surname, phone, status, timestamp):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO attendance (name, surname, phone, status, timestamp) VALUES (?, ?, ?, ?, ?)',
              (name, surname, phone, status, timestamp))
    conn.commit()
    conn.close()

def get_all_attendance():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT name, surname, phone, status, timestamp FROM attendance ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    return rows

# --- Basic Auth for admin page ---
def check_auth(username, password):
    return username == 'admin' and password == 'secret123'  # Change credentials here

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

# --- Routes ---
@app.route('/')
def home():
    return '<h1>Welcome to the Church Attendance Tracker</h1>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone = request.form['phone']
        status = request.form['status']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        insert_attendance(name, surname, phone, status, timestamp)
        return render_template('gratitude.html', name=name)

    return render_template('form.html')

@app.route('/admin')
def admin():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

    rows = get_all_attendance()
    return render_template('admin.html', records=rows)

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
