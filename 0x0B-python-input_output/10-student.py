#!/usr/bin/python3
"""class module of student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initializing attrs

        args:
            first_name: 1st name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """to json function

        args:
            attrs: list of string
        """
        final_dic = {}
        if type(attrs) is not list:
            return self.__dict__
        for i in range(len(attrs)):
            if attrs[i] in self.__dict__:
                final_dic[attrs[i]] = self.__dict__[attrs[i]]
        return final_dic
