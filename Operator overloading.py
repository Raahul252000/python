"""
Operator Overloading means giving extended meaning beyond their predefined operational meaning.
 For example operator + is used to add two integers as well as join two strings and merge two lists.
 It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that
 the same built-in operator or function shows different behavior for objects of different classes, this is called
 Operator Overloading.
"""

class Employee:
    no_of_leaves = 6

    def __init__(self,name,age,salary,role):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.Name},Age is {self.age}, Salary is {self.salary} and role is {self.role}."

    # '+' operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    # '-' operator overloading
    def __sub__(self, other):
        return self.age - other.age

    # '<' operator overloading
    def __lt__(self, other):
        return self.age < other.age

rahul = Employee("rahul yadav",22,445,"Programmer")
amit = Employee("amit wadgare",32,350,"Programmer")

print(rahul+amit)
print(rahul.__add__(amit))
print(rahul-amit)
print(rahul.__sub__(amit ))
print(rahul.__lt__(amit))
print(rahul<amit)