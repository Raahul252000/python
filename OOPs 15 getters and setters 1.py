"""
@property is a decorator which means a function can be treated as an attribute. like we can access the method like an attribute
without parenthesis.

"""
# Example 1:
class employe:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    @property       # this is getter.
    def get_email(self):               # because of @property deco, now get_email can be accessed as an attribute but cannot be set like an attribute.
        return self.firstname + "." + self.lastname + "@gmail.com"

    @get_email.setter              # with the help of setter we can set the method get_email like an attribute.
    def get_email(self,email):
        list1 = email.split("@")[0].split(".")
        self.firstname = list1[0]
        self.lastname = list1[1]

aman = employe("aman","gupta")

print(aman.firstname)
print(aman.lastname)
print(aman.get_email)

aman.firstname = "vicky"
print(aman.get_email)

aman.get_email = "chota.don@gmail.com"

print(aman.get_email)
print(aman.firstname)
print(aman.lastname)
