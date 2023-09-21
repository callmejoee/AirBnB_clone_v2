import unittest
from models.engine.db_storage import DBStorage
from models.user import User

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        self.db.close()

    def test_all(self):
        all_objects = self.db.all()
        self.assertIsInstance(all_objects, dict)
        all_users = self.db.all(User)
        self.assertIsInstance(all_users, dict)

if __name__ == '__main__':
    unittest.main()
