"""A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result."""
# In Python a function is defined using the def keyword:
# To call a function, use the function name followed by parenthesis:

def greet():
    print("Hello sir!")
    print("How are You!")

def average(a,b):
    avrg = (a+b)/2
    print(avrg)
    return avrg
def capital(x):
    y = x.upper()
    print(y)

def fix(z):
    """ this is a function which capitalize the first letter of every word."""
    x=z.capitalize()
    print(x)


capital("this is rahul")
greet()
average(12,34)
fix("i dont know if its gonna work.")

# what is docstrings ?
"""Python documentation strings (or docstrings) provide a convenient way of associating documentation with 
Python modules, functions, classes, and methods.
It’s specified in source code that is used, like a comment, to document a specific segment of code. 
Unlike conventional source code comments, the docstring should describe what the function does, not how."""


def average(a,b):
    """This is a function which return average of two number. """
    avrg = (a+b)/2
    return avrg
v=average(9,56)
print(v)
print(average.__doc__)   # this is how we can find out what functions do.
print(fix.__doc__)