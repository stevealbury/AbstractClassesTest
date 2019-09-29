# import a dummy class from the special Python module
# you cannot create objects from this class
# it just sets the rules for classes inheriting from it
# abc = "abstract base class
from abc import ABC


class Shape( ABC ):

    # this annotation tells system this method is not instantiable
    # the keyword "pass" means DO NOTHNG
    # so it means any class inheriting from this MUST create it's own version
    # of the function
    @classmethod
    def shapeArea(self): pass

    @classmethod
    def shapeBoundary(self): pass


# here is our own class
class Square( Shape ):
    __side: int

    # the double underscore here just means it is internal - in this case init is Python's
    # way of writing constructors - the code that builds an object in memory
    def __init__(self, side):
        self.__side = side

    def shapeArea(self):
        self.__area = self.__side * self.__side
        return self.__area

    def shapeBoundary(self):
        return 4 * self.__side


# create and print a square
mySquare = Square( 10 )
print( mySquare.shapeArea() )
print( mySquare.shapeBoundary() )
