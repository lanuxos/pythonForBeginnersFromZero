# ep9 - OOP
# abstract
from abc import ABC, abstractmethod

class Rectangle(ABC):
    @abstractmethod
    def calculate(self):
        pass
class Rectanglar(Rectangle):
    def __init__(self, width, length, depth):
        self.width = width
        self.length = length
        self.depth = depth
    def calculate(self): # overide method
        return self.width * self.length * self.depth

if __name__ == '__main__':
    rect = Rectanglar(2,3,5)
    print(rect.calculate())