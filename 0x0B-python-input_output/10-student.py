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

    
    def to_json(self, attrs=None):
        """retrieves dictionary of an object

        args:
            attrs: list of strings
        """
        final_dic = {}
        if type(attrs) is not list:
            return self.__dict__
        for i in range(len(attrs)):
            if attrs[i] in self.__dict__:
                final_dic[attrs[i]] = self.__dict__[attrs[i]]
        return final_dic
