"""
Scope refers to the coding region from which a particular Python object is accessible. Hence one cannot access
any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.

There are four types of scopes:
1.local: Contains names defined inside the current function. if we define any variable inside a function then the scope
of the variable is inside that function. when the functions ends the availability of the variables ends.

2.Global: Contains names Defined at the top level of the scripts or module. And these names are available for the whole
script, lifetime of the variables ends when the program ends. the variable in this scope is known as global variable.

3.enclosed: Contains Names defined inside any and all enclosed function. a function inside a function is known as enclosed
function and in that enclosed function defined variables are known as enclosed variables.

4.Built-in scope: Contains names built in to the python language.

"""
# Example: local scope

def func():
    x = 5   # local variable
    print(x)
func()
# print(x)   if i try to access the variable x from outside of the fucntion it will give the error because its not its scope.
