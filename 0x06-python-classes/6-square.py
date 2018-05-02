#!/usr/bin/python3


class Square:
        """Creating a class called Square"""
        def __init__(self, size=0, position=(0, 0)):
                """Creating a special method for Square"""
                self.__size = size
                self.__position = position

        def area(self):
                """Creating a public instance method called area"""
                return self.__size * self.__size

        def my_print(self):
                """Creating a public instance method called my_print"""
                if self.__size == 0:
                        print()
                for m in range(self.__position[1]):
                        print()

                for j in range(self.__size):
                        print("{}{}".format(" " * self.__position[0], "#" * self.__size), end="")
                        print()

        def position(self, size=0, position=(0, 0)):
                """Creating a public instance method called position"""
                return self.__position

        @property
        def size(self):
                """Property for attribute size"""
                return self.__size

        @size.setter
        def size(self, value):
                """Setter for attribute size"""
                if type(value) != int:
                        print("size must be an integer", end="")
                        raise TypeError
                elif value < 0:
                        print("size must be >= 0", end="")
                        raise ValueError
                else:
                        self.__size = value

        @property
        def position(self):
                """Property for attribute position"""
                return self.__position

        @position.setter
        def position(self, value):
                """Setter for attribute position"""
                if type(value) is tuple and len(value) == 2 and type(value[0]) is int\
                and type(value[1]) is int and value[0] > 0 and value[1] > 0:
                        self.__position = value
                else: 
                        print("position must be a tuple of 2 positive integers", end="")
                        raise TypeError
