import unittest
from models.base_model import Base
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        self.db.close()
        
    
    def test_all():
        all_objects = self.db.all()
        self.assertIsInstance(all_objects, dict)  
        all_users = self.db.all(User)
        self.assertIsInstance(all_users, dict)
