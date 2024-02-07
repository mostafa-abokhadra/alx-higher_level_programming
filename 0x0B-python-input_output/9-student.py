#!/usr/bin/python3
"""student class module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initializing attributes

        args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary of an object"""
        return dict(self.__dict__)
