#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

print(fs.all())
s = State()
print(s.to_dict['__class__'])
