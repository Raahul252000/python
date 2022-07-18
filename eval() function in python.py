"""
eval():this function evaluates python expression which are written as strings.
syntax: eval(expression,globals=None,locals=None)
"""

# ex:1
a = "2*5+4*5"
print(eval(a))

# input() inside eval()
# print(eval(input("Enter the expression: ")))

# globals arguments should be in the key:value pair
print(eval("a+b+a**2+b**2",{"a":2,"b":4}))

# globals
# print(eval(input("enter the expression: "),{"a":eval(input("enter the value of a:")),"b":eval(input("enter the value of b:"))}))

# eval() can take arguments declared outside the eval function.
a = 10
b = 2
print(eval("a**b"))

#
a = eval(input("enter the value: "))
print(a,type(a))
b = eval(input("enter the value: "))
print(b,type(b))