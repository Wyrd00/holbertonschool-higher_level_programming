#!/usr/bin/python3
"""

Module with one class: Square

"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """
    class Square that inherits class Rect
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square constructor method
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """override string of Square"""
        return "[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update square self"""
        arg = len(args)

        if arg:
            if arg > 0:
                self.id = args[0]
            if arg > 1:
                self.size = args[1]
            if arg > 2:
                self.x = args[2]
            if arg > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """dictionary representaton of Sqaure"""
        newdict = {}
        newdict['id'] = self.id
        newdict['size'] = self.height
        newdict['x'] = self.x
        newdict['y'] = self.y
        return newdict
