#!/usr/bin/python3
"""

Module contain one class: Rectangle

"""
from models.base import Base


class Rectangle(Base):
    """make rectangle, inherit class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor for Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rect"""
        return self.width * self.height

    def display(self):
        """print visual representation of rect"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print("{}{}".format(self.x * " ", "#" * self.width))

    def __str__(self):
        """override str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """reassign attribute with arg"""
        arg = len(args)

        if arg:
            if arg > 0:
                self.id = args[0]
            if arg > 1:
                self.width = args[1]
            if arg > 2:
                self.height = args[2]
            if arg > 3:
                self.x = args[3]
            if arg > 4:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
                #self.__dict__[k] = v

    def to_dictionary(self):
        """dict representation of Rectangle"""
        newdict = {}
        newdict['id'] = self.id
        newdict['height'] = self.height 
        newdict['width'] = self.width
        newdict['x'] = self.x
        newdict['y'] = self.y
        return newdict
