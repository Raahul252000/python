class A:
    classvar1 = " I am a class varialble inside class A. "
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "I am a instance varriable in class A"
        self.specialvar = "I am the special variable inside class A"
class B(A):
    classvar1 = "I am a class variable insdie class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I am a instance varriable in class B"
        super().__init__()
x = A()
y = B()
print(y.specialvar,y.var1,y.classvar1)