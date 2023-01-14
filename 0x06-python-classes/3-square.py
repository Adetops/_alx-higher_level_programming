#!/usr/bin/python3

"""Define a class square"""
class Square:
    """Private attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    """Public method"""
    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
