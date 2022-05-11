class Employee:
    no_of_leaves = 6   #class variable.

    def __init__(self,name,age,salary,role):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.Name},Age is {self.age}, Salary is {self.salary} and role is {self.role}"


# CONSTRUCTORS: A constructor is a special type of method (function) which is used to initialize
# the instance members of the class.
# In C++ or Java, the constructor has the same name as its class, but it treats constructor differently in Python.
# It is used to create an object.
# Constructors can be of two types.
# Parameterized Constructor
# Non-parameterized Constructor
# Constructor definition is executed when we create the object of this class. Constructors also verify that there are
# enough resources for the object to perform any start-up task.

rahul = Employee("Rahul Yadav",22,"96k","Software Developer")
bhakti = Employee("Bhakti singh",25,"67k","Data Analyst")

print(rahul.Name)
print(rahul.age)
print(bhakti.__dict__)
print(rahul.__dict__)
print(rahul.printdetails())
print(bhakti.printdetails())