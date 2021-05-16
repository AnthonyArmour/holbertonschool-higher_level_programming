#!/usr/bin/python3
"""Square class inherits from Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method for square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return printablbe instance"""
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width))
