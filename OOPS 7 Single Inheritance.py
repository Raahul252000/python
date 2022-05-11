class Employee:
    no_of_leaves = 6   #class variable.

    def __init__(self,name,age,salary,role):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.Name},Age is {self.age}, Salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def obj_from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def greet(string):
        print("Hello!!! welcome "+string)

class Programmer(Employee):
    no_of_leaves = 45

    def __init__(self,name,age,salary,role,language):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role
        self.language = language


    def printprog(self):
        return f"The programmer's name is {self.Name}, age is {self.age}, Salary is {self.salary}, role is {self.role} and languages are {self.language}."


harry = Employee("Harry",27,"65k","Instructor")
print(harry.printdetails())

rahul = Programmer("Rahul Yadav",22,"100k","Programmer",["python","SQL","html"])
karan = Programmer("Karan",22,"90k","Programmer",["Java","SQL"])
print(rahul.printdetails())
print(karan.printprog())
print(rahul.printprog())
print(rahul.no_of_leaves)