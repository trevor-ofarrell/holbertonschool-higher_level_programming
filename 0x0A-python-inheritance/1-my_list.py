#!/usr/bin/python3
class MyList(list):

    """class that inherits from list super-class"""

    def print_sorted(self):

        """prints sorted list"""

        print(sorted(self))
