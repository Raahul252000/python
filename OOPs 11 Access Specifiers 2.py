class Staff:
    no_of_employes = 0

    def __init__(self,name,age,role):
        self._name = name
        self._age = age
        self._role = role
        self.update_staff()

    def __printdetails(self):
        return f" Name is {self._name}\n Age is {self._age}\n Role is {self._role}"
    
    @classmethod
    def update_staff(cls):
        cls.no_of_employes +=1

sam = Staff("Sam roy",25,"Programmer")
print(sam.printdetails())
sita = Staff("sita singh",27,"accountant")
tony = Staff("tony sharma",21,"junior programmer")
print(Staff.no_of_employes)
print(Staff.update_staff())
print(sam._name)
print(Staff.no_of_employes)
Rahul = Staff("Rahul Yadav",22,"Software Developer")
print(Staff.no_of_employes)