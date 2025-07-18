import sqlite3
from flask import Flask, render_template, request, Response, redirect, url_for
import csv
from io import StringIO
from datetime import datetime

app = Flask(__name__)

DB = 'yaf_attendance.db'

def get_db():
    conn = sqlite3.connect(app.config.get('DATABASE', DB))
    return conn

# --- Database helper ---
def insert_attendance(name, surname, phone, status, timestamp):
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO attendance (name, surname, phone, status, timestamp) VALUES (?, ?, ?, ?, ?)',
              (name, surname, phone, status, timestamp))
    conn.commit()
    conn.close()

def get_filtered_attendance(name=None, status=None, date=None):
    conn = get_db()
    c = conn.cursor()

    query = 'SELECT name, surname, phone, status, timestamp FROM attendance WHERE 1=1'
    params = []

    if name:
        query += ' AND name LIKE ?'
        params.append(f'%{name}%')
    if status:
        query += ' AND status = ?'
        params.append(status)
    if date:
        query += ' AND DATE(timestamp) = ?'
        params.append(date)

    query += ' ORDER BY timestamp DESC'
    c.execute(query, params)
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
    return redirect(url_for('form'))

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

    name = request.args.get('name')
    status = request.args.get('status')
    date = request.args.get('date')

    rows = get_filtered_attendance(name, status, date)
    return render_template('admin.html', records=rows)

@app.route('/admin/export')
def export_csv():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

    name = request.args.get('name')
    status = request.args.get('status')
    date = request.args.get('date')

    rows = get_filtered_attendance(name, status, date)

    # Create CSV in memory
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['First Name', 'Surname', 'Phone', 'Status', 'Timestamp'])
    writer.writerows(rows)

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment;filename=attendance_records.csv'}
    )

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
