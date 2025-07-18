import unittest
from attendance import app, get_db
import tempfile
import os

class AttendanceTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temp DB file
        self.db_fd, self.temp_db = tempfile.mkstemp()
        app.config['DATABASE'] = self.temp_db
        app.config['TESTING'] = True
        self.client = app.test_client()

        # Initialize DB schema
        with app.app_context():
            conn = get_db()
            c = conn.cursor()
            c.execute('''CREATE TABLE attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone TEXT NOT NULL,
                status TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )''')
            conn.commit()
            conn.close()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.temp_db)

    def test_home_page(self):
        rv = self.client.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Welcome to the YAF WCI Krugersdorp Attendance Tracker', rv.data)

    def test_form_get(self):
        rv = self.client.get('/form')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'First Name', rv.data)

    def test_form_post(self):
        rv = self.client.post('/form', data=dict(
            name='John',
            surname='Doe',
            phone='1234567890',
            status='first-timer'
        ), follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Thank you for gracing us with your presence, John!', rv.data)

    def test_admin_auth_required(self):
        rv = self.client.get('/admin')
        self.assertEqual(rv.status_code, 401)  # Unauthorized without auth

if __name__ == '__main__':
    unittest.main()
