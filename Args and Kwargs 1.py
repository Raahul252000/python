""" # *args and **kwargs
If you do not know how many arguments that will be passed into your function, add a * before the parameter name
 in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def funt_args(*args):
    print(args)
    for item in args:
        print(item)

stud = ["rahul","sam","rohan","jenny","sonu","tina"]
funt_args(*stud)

def funt_args1(a, *args,**kwargs):
    print(a)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

list1 = [34,12,21,43,22,"ram","aryan"]

kw = {"rahul":"programmer","jenny":"singer","monu":"dancer","tina":"cook"}

a = "this is the first time i am using args."
funt_args1(a,*list1,**kw)
