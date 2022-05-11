"""
Protected Access Modifier:
The members of a class that are declared protected are only accessible to a class derived from it. Data members
of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

Private Access Modifier:
The members of a class that are declared private are accessible within the class only, private access modifier is
the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol
before the data member of that class.
"""

class Employee:
    no_of_leaves = 6
    _protec = 456
    __privat = "this is private variable."

    def __init__(self,name,age,salary,role):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.Name},Age is {self.age}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def obj_from_str(cls,string):
        return cls(*string.split("-"))

ram = Employee("Ram Kumar",34,"56k","assistance")
print(ram._protec)              # accessing the protected class.
print(ram._Employee__privat)    # this is how we can access the private variables.
