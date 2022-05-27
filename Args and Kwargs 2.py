# *args and **kwargs:

def funt_args(*args):
    print(type(args))
    print("the name of the student is ",args[0],"and age is ",args[1], "and the rollno is ",args[2])

funt_args("rahul",22,877876)

def funt_args2(*args):
    if len(args) == 3:
        print("the name is ",args[0],",age is ",args[1],"and he is from ",args[2] )
    else:
        print("the name is ", args[0], "and age is ",args[1])

funt_args2("jenny",21,"MCA")
funt_args2("sam",24,"btech")
funt_args2("tina",25)

""" **kwargs:
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def funt_kwarg(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key},{value}")

marklist = {"rahul":91,"sam":98,"tina":45,"tarun":67,"sita":99,"ram":100,"ravan":98,"nitesh":32,"seema":21}

funt_kwarg(**marklist)

# using all normal, args and kwargs arguments together:

def funt_kwarg(a,*args,**kwargs):
    print(a)
    print(type(args))
    for i in args:
        print(i)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key},{value}")

a = "this is the first time i am using all normal,args and kwargs together:"
lis1 = ["john",30,"king",44,56,"sumit"]

funt_kwarg(a,*lis1,**marklist)

