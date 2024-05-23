#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
def __init__(self):
self.id = str(uuid.uuid4())
self.created_at = datetime.now()
self.updated-at = datetime.now()
def __str__(self):
return f" [{self.__class__.__name__}] (self.id) (self__dict__)"
def save(self):
self.update_at = datetime.now()
def to_dict(self):
dict_copy = self.__dict__.copy()S
dict_copy["__class__"] = self.__class__.name__
dict_copy["created_at"] = self.created_at.isoformat()
dict_copy["updat:d_at"] = self.updated_at.isoformat()
return dict_copy
