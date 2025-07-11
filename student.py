import json

class Student:
    def __init__(self, roll, name, email, course, marks):
        self.roll = roll
        self.name = name
        self.email = email
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            'roll': self.roll,
            'name': self.name,
            'email': self.email,
            'course': self.course,
            'marks': self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data['roll'],
            data['name'],
            data['email'],
            data['course'],
            data['marks']
        )
