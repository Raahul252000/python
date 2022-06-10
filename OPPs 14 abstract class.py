"""
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods
that must be created within any child classes built from the abstract class.
By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining
Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract
and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated
 with the keyword @abstractmethod.
"""
# abstract class cannot be instantiated.

# Example 1:
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        return 0
    pass
class Bird(Animal):
    def move(self):
        print("i fly.")

class Human(Animal):
    def move(self):
        print("i walk and run.")

class Fish(Animal):
    def move(self):
        print("i swim.")

class Reptiles(Animal):
    def move(self):
        print("i crawl.")

sparrow = Bird()
rahul = Human()
catfish = Fish()
crocodile = Reptiles()

sparrow.move()
rahul.move()
catfish.move()
crocodile.move()

# Example 2:

from abc import ABC,abstractmethod

class figures(ABC):
    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def find_perimeter(self):
        pass

class square(figures):
    def __init__(self,side):
        self.side1 = side
        self.side2 = side

    def find_area(self):
        return self.side1 * self.side2

    def find_perimeter(self):
        return 4 * (self.side1)

class triangle(figures):
    def __init__(self,height,base,hyp):
        self.height = height
        self.base = base
        self.hypo = hyp

    def find_area(self):
        return 1/2 * (self.base * self.height)

    def find_perimeter(self):
        return self.hypo + self.height + self.base

sq = square(5)
tri = triangle(5,3,8)

print(sq.find_area())
print(sq.find_perimeter())
print(tri.find_area())
print(tri.find_perimeter())