#!/usr/bin/python3


class Square:
        """Creating a class called Square"""
        def __init__(self, size=0, position=(0, 0)):
                """Creating a special method for Square"""
                self.size = size
                self.position = position

        def area(self):
                """Creating a public instance method called area"""
                return self.__size * self.__size

        def my_print(self):
            """Creating a public instance method called my_print"""
            if self.size == 0:
                print()
            for m in range(self.position[1]):
                print()

            for j in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))

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
                        raise TypeError("size must be an integer")
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
                x, y = value
                """Setter for attribute position"""
                if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(x, int) and isinstance(x, int) \
                and x >= 0 and y >= 0:
                        self.__position = value
                else:
                    print("position must be a tuple of 2 positive integers")
                    raise TypeError
