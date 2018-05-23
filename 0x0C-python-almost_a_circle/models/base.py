#!/usr/bin/python3
"""

MOdule with one class: Base

"""
import json


class Base:

    """
    Base of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method takes list_dict and return JSON rep
        need to be called as "Base.to_json_string b/c staticmethod
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        static method takes json string and return as python obj
        need to be called as "Base.from_json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json rep of list_objs to a file
        list_objs is a list of instances from Base inheritence
            ex: list of Square or list of Rect
        """
        list_dict = []
        for i in range(len(list_objs)):
            list_dict.append(list_objs[i].to_dictionary())
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """
        create dummy instance, then update it. Return accurate instance
        """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 2)
        else:
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """
        class method that returns list of instances, loaded from a file
        """
        filename = cls.__name__ + ".json"
        new = []
        try:
            with open(filename, "r", encoding='utf-8') as f:
                hoho = f.read()
                hoho_obj = cls.from_json_string(hoho)
                for i in range(len(hoho_obj)):
                    new.append(cls.create(**hoho_obj[i]))
        except:
            pass
        return new
