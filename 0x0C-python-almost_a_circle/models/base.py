#!/usr/bin/python3
"""Define class Base"""
import json


class Base:
    """Base class for other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        class_name = cls.__name__
        file_name = class_name + ".json"
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(obj_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return []
