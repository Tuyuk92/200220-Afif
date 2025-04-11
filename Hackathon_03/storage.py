import json
import os
from employee import Employee

class Storage(object):

    def __init__(self, filepath="employees.json"):
        self.filepath = filepath

    def save(self, employee):
        with open(self.filepath, 'w') as f:
            json.dump([emp.to_dict() for emp in employee], f, indent=4)

    def load(self):
        if not os.path.exists(self.filepath):
            return[]
        with open(self.filepath) as f:
            return [Employee.from_dict(data) for data in json.load(f)]