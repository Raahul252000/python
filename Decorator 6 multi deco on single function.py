"""
if multiple decorator acts on a single function, then the inner decorator works first and outer decorator acts on the
result of the inner decorator.
"""
# Example 1:
def upper_deco(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def split_deco(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_deco
@upper_deco               # phele @upper_deco decorator work krega phir iske result ko @split_deco decorate krega.
def greet():
    return "good morning"

print(greet())


# Example 2:

def deco1(func):
    def inner():
        return "first " + func() + " first"
    return inner

def deco2(func):
    def inner():
        return "second " + func() + " second"
    return inner

@deco2
@deco1
def greet():
    return "good morning"

print(greet())