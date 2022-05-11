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

class Player:

    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f" The name is {self.name}, Game is {self.game}"

class CoolProgrammer(Employee,Player):   # Employee is the 1st argument therefore coolprogrammer will use the constructor of Employee.

    language = "C++"

    def printlang(self):
        print(self.language)



Rahul = Employee("Rahul Yadav",22,"45k","Programmer")

Sumit = Player("Sumit Singh",["Cricket",])

karan = CoolProgrammer("karan",25,"100k","Coolprogrammer")

print(karan.printdetails())
karan.printlang()
