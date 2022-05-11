"""
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods
that must be created within any child classes built from the abstract class.
By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining
Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract
and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated
 with the keyword @abstractmethod.
"""
# abstract class cannot be instantiated.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        return 0
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