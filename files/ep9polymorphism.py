# ep9 - OOP
# polymorphism
from abc import ABC, abstractmethod

class Geometry(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def calArea(self):
        pass

class Triangle(Geometry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return 0.5 * self.base * self.height

class Parallel(Geometry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return self.base * self.height

class Rhombus(Geometry):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calArea(self):
        return self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(2, 5)
    print(triangle.base)
    parallel = Parallel(2, 3)
    print(parallel.calArea())
    rhombus = Rhombus(2, 3)
    print(rhombus.calArea())
