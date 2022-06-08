"""
Protected Access Modifier:
The members of a class that are declared protected are only accessible from within the base class and from derived class. Data members
of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

"""
# protected class

class automobile:
    _headlights = 2
    def __init__(self,doors,wheels,engine):
        self._doors = doors
        self._wheels = wheels
        self._engine = engine

tata = automobile(2,6,"petrol")
print(tata._wheels)
print(tata._engine)              # protected variable can be accessed within from base class.
tata._wheels = 12                # Protected variable can be modified from the base class.
print(tata._wheels)
class car(automobile):
    def __init__(self,doors,windows,wheels,engine,horsepower):
        super().__init__(doors,wheels,engine)
        self._windows = windows
        self._horsepower = horsepower

audi = car(4,4,4,"diesel",899)

print(audi._windows)
print(audi._doors)                      # protected var can be used from the inherited/sub-class as well.
print(audi._engine)
print(audi._wheels)
print(audi._horsepower)

audi._wheels  = 6
print(audi._wheels)                     # protected var can be modified as well from the inherited/sub_class.
