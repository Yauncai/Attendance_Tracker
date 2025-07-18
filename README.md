# Church Attendance Tracker

A modern web-based attendance management system for churches, designed to simplify attendance tracking through QR code check-ins, digital forms, and administrative tools.

## What is the Church Attendance Tracker?

The Church Attendance Tracker is a Python + Flask application that replaces traditional roll calls or paper sign-in sheets with a digital check-in system. Congregants scan a QR code and submit their details via a mobile-friendly form. Attendance data is stored in a structured database and available for analysis or download by administrators.

## What Does It Do?

The system provides the following core functionality:

### **Digital Check-In Process**
- Members scan a QR code and complete a short form.

- Attendance is time-stamped and stored automatically.


### **Personalized Welcome Messages**
- First-time visitors receive a custom welcome message.

- Regular attendees are greeted with a "welcome back."

### **Database Management**
- Stores attendance data in a persistent SQLite database.

- Prevents duplicate check-ins based on name and phone number.

### **Admin Dashboard**
- View a live table of all attendance records.

- Filter attendance by status (e.g., first-timers, regulars).

- Export attendance data as a CSV file.

- Responsive design for desktop and mobile views.

## How to Use the System

### **For Church Staff/Administrators**

- Visit /admin to view all records.

- Use filters to sort data.

- Export a .csv file for reporting or backups.

### **For Church Members and Visitors**

- Scan the QR code provided at the entrance.

- Fill out the form: name, phone number, and attendance status.

- Receive a welcome message based on your status.

### **Key Benefits**

- **Efficiency**: Eliminates manual attendance tracking and data entry
- **Accuracy**: Reduces human error in recording attendance
- **Accessibility**: Works with any smartphone - no special app required
- **Privacy**: Collects only essential information needed for church records
- **Hospitality**: Provides immediate, personalized welcome messages
- **Analytics**: Enables data-driven decisions about services and outreach
- **Follow-up**: Helps identify first-time visitors for pastoral care

## Technical Requirements

- Python 3.7 or higher
- Web framework (Flask/Django)
- Database system (SQLite3)
- QR code generation library
- Web server capability
- Internet connection for attendees to access the form

## Getting Started

1. Clone the repository, cd into the directory and create virtual environment: `python -m venv venv`
`source venv/bin/activate  # or venv\Scripts\activate on Windows`
2. Install dependencies: `pip install -r requirements.txt`
3. Activate the script: `chmod +x run_all.sh`
5. Run the script: `./run_all.sh`

## Support and Customization

The system is designed to be flexible and can be customized to meet your church's specific needs, including:
- Custom welcome messages
- Additional data fields
- Integration with existing church management systems
- Branded interface design
- Multi-language support

---

*This attendance tracker helps churches embrace digital tools while maintaining the personal touch that makes each visitor feel welcome and valued.*