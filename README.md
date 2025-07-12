# Church Attendance Tracker

A digital attendance management system designed to streamline church attendance tracking through QR code scanning and automated data collection.

## What is the Church Attendance Tracker?

The Church Attendance Tracker is a Python-based application that modernizes the traditional attendance-taking process in churches. Instead of manual paper-based systems or verbal roll calls, this system uses QR codes to allow congregation members to quickly check themselves in using their mobile devices.

## What Does It Do?

The system provides the following core functionality:

### **Digital Check-In Process**
- Generates QR codes that can be displayed at church entrances or in bulletins
- Allows attendees to scan the code with their smartphones
- Presents a simple web form for attendees to enter their information
- Automatically timestamps each check-in with the current date and time

### **Data Collection**
- Captures essential attendee information including:
  - Full name (first name and surname)
  - Phone number
  - First-time visitor status (first-timer vs. regular attendee)
  - Attendance date and time

### **Personalized Welcome Messages**
- **First-time visitors** receive a warm welcome message thanking them for visiting
- **Regular attendees** receive a "welcome back" message acknowledging their continued participation
- Messages can be customized to reflect your church's tone and hospitality

### **Database Management**
- Stores all attendance data in a structured database
- Maintains historical records for analysis and follow-up
- Ensures data integrity and prevents duplicate entries

### **Reporting and Analytics**
- Generate attendance reports by:
  - **Daily**: See who attended on specific dates
  - **Monthly**: Track attendance trends over months
  - **Yearly**: Analyze annual attendance patterns
- Get attendance counts and statistics for any time period
- Identify first-time visitors for follow-up and outreach

## How to Use the System

### **For Church Staff/Administrators**

1. **Setup and Installation**
   - Install Python and required dependencies
   - Configure the database connection
   - Set up the web server to handle QR code requests

2. **Generate QR Codes**
   - Create QR codes for each service or event
   - Display codes at church entrances, in bulletins, or on screens
   - Each QR code links to the attendance form

3. **Monitor Attendance**
   - View real-time check-ins as they happen
   - Access the admin dashboard to see current attendance
   - Generate reports for leadership and planning purposes

### **For Church Members and Visitors**

1. **Scan the QR Code**
   - Use your smartphone camera or QR code reader app
   - Scan the code displayed at the church entrance or in materials

2. **Complete the Form**
   - Enter your first name and surname
   - Provide your phone number
   - Select whether you're a first-time visitor or regular attendee
   - Submit the form

3. **Receive Confirmation**
   - Get an immediate welcome message
   - Your attendance is automatically recorded
   - No additional steps required

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
- Database system (SQLite/PostgreSQL/MySQL)
- QR code generation library
- Web server capability
- Internet connection for attendees to access the form

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your database settings
4. Run the application: `python app.py`
5. Generate and display QR codes for your services
6. Start collecting attendance data digitally

## Support and Customization

The system is designed to be flexible and can be customized to meet your church's specific needs, including:
- Custom welcome messages
- Additional data fields
- Integration with existing church management systems
- Branded interface design
- Multi-language support

---

*This attendance tracker helps churches embrace digital tools while maintaining the personal touch that makes each visitor feel welcome and valued.*