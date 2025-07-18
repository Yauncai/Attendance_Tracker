# import unittest
# from attendance import app

# class EdgeCaseTests(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_empty_fields(self):
#         response = self.app.post('/form', data={
#             'name': '',
#             'surname': '',
#             'phone': '',
#             'status': 'first-timer'
#         })
#         self.assertIn(b'This field is required', response.data)  # or check for redirect or error handling

#     def test_invalid_phone_letters(self):
#         response = self.app.post('/form', data={
#             'name': 'John',
#             'surname': 'Doe',
#             'phone': '123ABC4567',
#             'status': 'regular'
#         })
#         self.assertIn(b'Invalid phone number', response.data)

#     def test_invalid_status(self):
#         response = self.app.post('/form', data={
#             'name': 'Jane',
#             'surname': 'Doe',
#             'phone': '1234567890',
#             'status': 'visitor'  # invalid status
#         })
#         self.assertIn(b'Invalid status', response.data)

#     def test_sql_injection(self):
#         response = self.app.post('/form', data={
#             'name': "Robert'); DROP TABLE attendance;--",
#             'surname': 'Smith',
#             'phone': '1234567890',
#             'status': 'regular'
#         })
#         # Should not drop table, maybe check for success or safe handling
#         self.assertEqual(response.status_code, 200)

#     def test_long_names(self):
#         long_name = 'a' * 300
#         response = self.app.post('/form', data={
#             'name': long_name,
#             'surname': long_name,
#             'phone': '1234567890',
#             'status': 'first-timer'
#         })
#         self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()
