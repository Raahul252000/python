"""
if we want to pass parameters in the decorator then we have to make one more function above the decorator which will
take the parameters.
"""

# Example 1:
def outer(expression):
    def my_deco(func):
        def inner():
            return func() + expression
        return inner
    return my_deco

@outer(expression= "rahul yadav")
def greet():
    return "Hello, good morning "

print(greet())