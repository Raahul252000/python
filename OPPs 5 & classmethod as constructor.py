
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

karan = Employee.obj_from_str("karan-35-56k-data scientist")
print(karan.salary)
print(karan.__dict__)
rahul = Employee.obj_from_str("rahul-22-95k-software developer")
print(rahul.__dict__)
print(Employee.no_of_leaves)
Employee.change_leaves(45)
print(Employee.no_of_leaves)