# def getName():
#     name = input("What is your name?: ")
    
#     while not  name.isalpha():
#         name = input("What is your name?: ")

#     return name
    

# def getSurname():
#     surname = input("What is your surname?: ")
    
#     while not surname.isalpha():
#         surname = input("What is your surname?: ")

#     return surname
    

# def getPhoneNumber():
#     number=input("What is your number?: ")

#     while not number.isdigit() or  len(number) !=10:
#         number=input("What is your number?: ")
    
#     return number
    
        
        



# if __name__ == '__main__':
#     getName()
#     getSurname()
#     getPhoneNumber()

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Church Attendance Tracker</h1>'

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
        return f"Thank you for checking in, {name}!"
    
    return '''
        <form method="POST">
            First Name: <input type="text" name="name" required><br>
            Surname: <input type="text" name="surname" required><br>
            Phone Number: <input type="tel" name="phone" required><br>
            Are you a:
            <select name="status">
                <option value="first-timer">First-time visitor</option>
                <option value="regular">Regular attendee</option>
            </select><br>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
