import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.first_name = "3mk Joe"
        self.user.last_name = "3mk Joe bardo"
        self.user.email = "guesswhat?3mkjoe@gmail.com"
        self.user.password = "123456"

    def tearDown(self):
        del self.user

    def test_email_type(self):
        self.assertIsInstance(self.user.email, str)

    def test_password_type(self):
        self.assertIsInstance(self.user.password, str)

    def test_first_name_type(self):
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_type(self):
        self.assertIsInstance(self.user.last_name, str)

    def test_email(self):
        self.assertEqual(self.user.email, "guesswhat?3mkjoe@gmail.com")

    def test_password(self):
        self.assertEqual(self.user.password, "123456")

    def test_first_name(self):
        self.assertEqual(self.user.first_name, "3mk Joe")

    def test_last_name(self):
        self.assertEqual(self.user.last_name, "3mk Joe bardo")

if __name__ == "__main__":
    unittest.main()

