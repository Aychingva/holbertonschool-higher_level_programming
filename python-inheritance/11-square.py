#!/usr/bin/python3
"""Module that defines Square class with str method."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def __init__(self, size):
        """Instantiates Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
