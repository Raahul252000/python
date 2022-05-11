
class Employee:
    no_of_leaves = 6   #class variable.

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

    @staticmethod
    def greet(string):
        print("Hello!!! welcome "+string)
"""
@staticmethod helps to create a types of methods which will deal with neither the class variable nor the instance variable
and also staticmethod neither takes class as a first argument nor the self as a first argument.
we can use staticmethod with help of the class as well as instance.

"""

sumit = Employee("Sumit singh",34,"45k","Sports Teacher")

print(sumit.Name,sumit.role)
sumit.greet("rahul")
Employee.greet("ra")

#Defination of static method:
