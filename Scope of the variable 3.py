
# the outer function is known is enclosing function and everything inside the enclosing function comes under enclosing scope.

# Example 5: Enclosing scope and enclosing variable:
print("Example 5:")

y = 10           # global variable
def outer_fun():
    z = 15       # enclosed variable: a variable inside the outer function/enclosing function.
    def inner_fun():
        x = 4    # local variable
        print("x:",x)
        print("inside the inner function z:",z)       # we can access the enclosed variable from the local scope.
    inner_fun()
    print(x)
    print("z:",z)

outer_fun()
# note: we can access the enclosed variable from the local scope but we can not acces the local variable from the enclosing scope. because we can access the variable in its scope only.


# Example 6: what if we try to modify the enclosed variable from local scope?
             # Ans: we will get error, because local scope is not allowed to modify the enclosed variable.

print("Example 6:")
y = 10           # global variable
def outer_fun():
    z = 15       # enclosed variable: a variable inside the outer function/enclosing variable.
    def inner_fun():
        x = 4    # local variable
        print("x:",x)
        nonlocal z
        z = z+1
        print("inside the inner function z:",z)       # we can access the enclosed variable from the local scope.
    inner_fun()
    print("z:",z)

outer_fun()

# note: we can modify the enclosed variable from the local scope provided that first we have to use the 'nonlocal' keyword.