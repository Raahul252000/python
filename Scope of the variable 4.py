# LEGB rule:

""" Q:if local variable, enclosed variable and global variable have the same name then how the python will get to know which
value should be printed?

ans: python always uses the LEGB to  deal with these kinds of problems.
     LEGB: LOCAL, ENCLOSED, GLOBAL, BUILT-IN.
This is the order of preference which python follow to search the variable.
"""

# Example: when the local, enclosed and global variable have the same name:

x = 5
def outer_fun():
    x = 10
    def inner_fun():
        x = 15
        print("x:",x)
    inner_fun()

outer_fun()

"""
working: firstly python will search for variable in local scope, if the variable is not present in local scope, it will 
look in enclosed scope, if still the variable is not there the it will look into the global scope, if still the variable is 
not there then it will look into the built-in scope and if the variable is still not present then finally it will throw the error at last.
"""