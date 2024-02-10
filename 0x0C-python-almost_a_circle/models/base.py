#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        name = list_objs[0].__class__.__name__
        name += ".json"
        with open(name, mode='w', encoding="utf-8") as fily:
            if list_objs:
                fily.write("[")
                for inst in list_objs:
                    dicty = inst.to_dictionary()
                    fily.write(cls.to_json_string(dicty))
                    if inst != list_objs[-1]:
                        fily.write(", ")
                fily.write("]")
            else:
                fily.write("[]")

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 4)
        if cls.__name__ == 'Square':
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

