#!/usr/bin/python3


class Square:
        """Creating a class called Square"""
        def __init__(self, size=0, position=(0, 0)):
                """Creating a special method for Square"""
                self.size = size
                self.position = position

        def area(self):
                """Creating a public instance method called area"""
                return self.size * self.size

        def my_print(self):
            """Creating a public instance method called my_print"""
            if self.size == 0:
                print()
                return
            for m in range(self.position[1]):
                print()

            for j in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))

        @property
        def size(self):
            """Property for attribute size"""
            return self.__size

        @size.setter
        def size(self, value):
                """Setter for attribute size"""
                if type(value) != int:
                        raise TypeError("size must be an integer")
                elif value < 0:
                        raise ValueError("size must be >= 0")
                else:
                        self.__size = value

        @property
        def position(self):
                """Property for attribute position"""
                return self.__position

        @position.setter
        def position(self, value):
                """Setter for attribute position"""
                if isinstance(value, tuple) and len(value) == 2 and \
                   isinstance(value[0], int) and isinstance(value[1], int) \
                   and value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                else:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
