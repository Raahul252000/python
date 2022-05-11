class Students:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        # self.email = f"{self.fistname}.{self.lastname}@gmail.com"

    def explain(self):
        return f"The name of the student is {self.firstname} {self.lastname}."
    @property
    def email(self):
        if self.firstname == None or self.lastname == None:
            return "Email is not set."
        else:
            return f"{self.firstname}.{self.lastname}@gmail.com"

    @email.setter
    def email(self,string):
        names = string.split("@")[0]       # split() will written the list.
        self.firstname = names.split(".")[0]
        self.lastname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.firstname = None
        self.lastname = None


anurag = Students("Anurag","Tripathi")
ankita = Students("Ankita","Asthana")
tina = Students("Tina","Rai")
print(ankita.email)

ankita.lastname = "lokhande"
print(ankita.email)
ankita.email = "thisisankita.sharma@gmail.com"
print(ankita.email)
print(ankita.lastname)

del ankita.email
print(ankita.email)
print(anurag.explain())
print(tina.email)
print(tina.firstname)
print(tina.lastname)