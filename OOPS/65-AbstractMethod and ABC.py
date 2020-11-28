# AbstractMethodBaseClass  --> like Rules
#import abc
from abc import ABC,abstractmethod
class Shape(ABC): # orABCMeta
    @abstractmethod
    def printDetails(self):
        return 0
class Square(Shape):
    type = "Square"
    size = 4
    def __init__(self):
        self.sidecm =10

    def printDetails(self):
        return f" Area of the square is {self.sidecm * self.sidecm}"
    # Suppose in drived class la printDetails illa na throwing error
    # TypeError: Can't instantiate abstract class Square with abstract method printDetails

s1 = Square()
print(s1.printDetails())
s2 = Shape()
#print(s2)
#TypeError: Can't instantiate abstract class Shape with abstract method printDetails
# we can't Create object for Abstract Method
