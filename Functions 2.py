"""
Python has the most interesting feature that everything is treated as an object even classes or any variable
we define in Python is also assumed as an object. Functions are first-class objects in the Python because they can
reference to, passed to a variable and returned from other functions as well.

We need to understand the following concept of the function:

1.The function can be referenced and passed to a variable and returned from other functions as well.

2.The functions can be declared inside another function and passed as an argument to another function.

note: whenever we pass a function into another function or we return a function from another function we always use the name
of the function without bracket '()'.
"""

# Example 1: the function can be referenced to a variable.

def printmsg(msg):
    print(msg)

printmsg("Hello, This is rahul here.")
x = printmsg          # printmsg function is referenced to x variable.
x("Hello, This is rahul here.")

"""note: if we delete the original function definition after referring to some variable, still the function
 will work because the definition of function has been copied into the variable."""

def printmsg(msg):
    print(msg)

x = printmsg                # printmsg function is referenced to x variable.
del printmsg
x("Hello bhai.")

# Example 2: passing functions into another function.

"""
a function that accepts other functions as a arguments is known as higher order function.
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def operations(fun,a,b):
    result = fun(a,b)
    print(result)

operations(add,4,5)
operations(sub,23,12)
operations(mul,25,5)
operations(div,45,8)

# Example 3: one function can be returned from another function:

def greet():
    def hii(): 
        print("Hello sir!!!")
    return hii

result = greet()
result()

# Example 4: with python one function can be defined into another function:

def greet():
    print("Hello sir!!!")
    def intro():
        print("we are here to assist you.")
    def ask():
        print("How can i help you sir.")
    intro()
    ask()

greet()