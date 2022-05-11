class Employe:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def explain(self):
        return f" This Employe is {self.fname} {self.lname} and his salary is {self.salary}"

    @property        # @property is a decorator which means a function can be deal as a attribute.
    def printemail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @printemail.setter
    def printemail(self,given_email):
        name_list = given_email.split("@")[0].split(".")     #split function returns the list of string.
        self.fname = name_list[0]    # here we are extracting the fname and lame from the given email and setting the email.
        self.lname = name_list[1]

# here printemail() was a function earlier but after using @property, printemail started behaving like an attribute and
# using @printemail.setter,we can directly set the email in the printemail like any other variable.


rohan = Employe("Rohan","Yadav",450)
amit = Employe("Amit","Sharma",500)

amit.lname = "khanna"
print(amit.printemail)
print(rohan.printemail)
print(amit.lname)
rohan.printemail = "Rohan.dubey@gmail.com"
print(rohan.lname)
print(rohan.printemail)
print(rohan.explain())