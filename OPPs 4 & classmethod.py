
class Employee:
    no_of_leaves = 6   #class variable.

    def __init__(self,name,age,salary,role):
        self.Name = name
        self.age = age
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.Name},Age is {self.age}, Salary is {self.salary} and role is {self.role}"

""" @classmethod decorators helps to create methods which will deal with the variable of the class not with 
the instance variable,
classmethods takes 1st argument 'class' not 'self'.

Class variable : class variables are those variables which are common for all the instance. With the help
of instance we can use the class variable but we cannot modify the class variable, therefore, we use @classmethod to
deal with or to make changes in class variable.

Instance variable: variables which have same name for all the instance of same class but store different values for 
different instance. 

"""


    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

Employee.change_leaves(50)
print(Employee.no_of_leaves)
karan = Employee("Karan",24,"60k","teacher")
print(karan.Name,karan.role)
karan.change_leaves(77)
print(Employee.no_of_leaves)