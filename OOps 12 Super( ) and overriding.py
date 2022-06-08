
# Example1:
class A:
    classvar1 = " I am a class variable inside class A. "
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "I am a instance variable in class A"
        self.specialvar = "I am the special variable inside class A"
class B(A):
    classvar1 = "I am a class variable inside class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I am a instance variable in class B"
        super().__init__()
x = A()
y = B()
print(y.specialvar,y.var1,y.classvar1)


# Example 2:

class person:
    classvar = "i am in the class person."
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

class employe(person):
    classvar = "i am in the class employe."
    def __init__(self,name,age,gender,role,salary):
        super().__init__(name,age,gender)
        self.role = role
        self.salary = salary

    def display(self):
        super().display()
        print("Role:",self.role)
        print("Salary:",self.salary)

rahul = employe("Rahul Yadav",22,"Male","SDE","566k")
rahul.display()

