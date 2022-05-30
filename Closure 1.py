"""
When enclosing function returns nested function without parentheses,then it becomes closure.

A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

criteria to create a closure:
1. must have a Nested function.
2. Nested function must refer values in enclosing scope.
3. enclosing function must return nested function.

Advantages of Closure:
1. can avoid global values.
2. data hiding.
"""

# Example 1:
def outer(x):
    def inner(y):         # local function to outer function.
        return x+y
    return inner
a = outer(5)
print(a(12))

# Example 2:
def nth_power(exponent):      # even if we delete the outer function still the inner function will remember the enclosed variable\nonlocal variable.
    def pow_of(base):
        print(pow(base,exponent))
    return pow_of

square = nth_power(2)
cube = nth_power(3)
square(3)
square(5)
square(7)
cube(3)
cube(5)
cube(7)

"""
1.As observed from the above code, closures help to invoke functions outside their scope.
2.The inner Function has its scope only inside the outer Function. But with the use of closures, 
we can easily extend its scope to invoke a function outside its scope.
"""