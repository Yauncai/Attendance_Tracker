from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to YAF WCI Krugersdorp Attendance Tracker</h1>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone = request.form['phone']
        status = request.form['status']  # first-timer or regular
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # For now, just print the data
        print(f"{name} {surname} ({status}) checked in at {timestamp} with number {phone}")
        return f"Thank you for gracing us with your presence, {name}!"
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
