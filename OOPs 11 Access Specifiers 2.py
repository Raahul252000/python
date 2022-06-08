"""
Private Access Modifier:
The members of a class that are declared private are accessible within the class only, private access modifier is
the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol
before the data member of that class.

"""
# private class:
class automobile:
    __headlights = 2
    def __init__(self,doors,wheels,engine):
        self.__doors = doors
        self.__wheels = wheels
        self.__engine = engine

    def __printdetails(self):
        print(f"The car has {self.__doors} doors,{self.__wheels} wheels and it has {self.__engine} engine.")

    def display(self):
        self.__printdetails()

truck = automobile(2,12,"diesel")
print(truck._automobile__wheels)            # private variable can't even accessed outside of the class with the help of object.
# truck._automobile__printdetails()

class car(automobile):
    def __init__(self,doors,wheels,engine,windows):
        super().__init__(doors,wheels,engine)
        self.windows = windows

mercedes = car(2,4,"petrol",2)

print(mercedes.windows)
print(mercedes._automobile__engine)
print(mercedes._automobile__wheels)
mercedes._automobile__wheels = 10

print(mercedes._automobile__wheels)
print(dir(mercedes))
# mercedes._automobile__printdetails()
mercedes.display()