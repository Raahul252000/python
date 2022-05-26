# Example 2: global scope and global variable:
print("Example 2:")
y = 10       # global variable
def func():
    x = 5    # local variable
    print(x)
    print("accessing 'y' from inside of the function:",y)
func()
print("y:",y)

# note: we can access global variable anywhere from the script.


# Example 3: if the local variable and global variable have same name:
print("Example 3:")
y = 10       # global variable
def func():
    x = 5    # local variable
    y = 7
    print(x)
    print("accessing 'y' from inside of the function:",y)     # if the name is same then the function will always give preference to its local variable.
func()
print("y:",y)


# Example 4: what if we try to modify the global variable from local scope:
             #ans: we will get error if we try to do so, because local scope doesn't allowed to change the global variable.
print("Example 4:")
y = 10       # global variable
def func():
    x = 5    # local variable
    global y        # with global keyword we give permission to local scope to modify the global variable.
    y = y+1
    print(x)
    print("accessing 'y' from inside of the function:",y)     # if the name is same then the function will always give preference to its local variable.
func()
print("y:",y)

# note: we can change the global variable from inside the local scope provided that first we have to global keyword.
