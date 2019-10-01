class Square:
    """ class to represent a square"""

    def __init__(self, size=0):

        """init method
        Attributes:
           attr1 (size) - size of square
        Raises:
           ValueError:  If size is negitive
           TypeError:  If size is not an int"""

        self.size = size

    def my_print(self):
        """Public instance method to print square based on area data"""
        if self.size == 0:
            print('\n')
        for i in range(self.size):
            for i in range(self.size):
                print("#", end='')
            print()

    def area(self):
        """Public instance method to return area of square"""
        return self.__size ** 2
