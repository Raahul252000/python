"""
Python has predefined functions for many mathematical, logical, relational, bitwise etc operations under
the module “operator”. Some of the basic functions are covered in this article.
"""
import operator
x,y = [int(i) for i in input("enter the two numbers: ").split()]
print(x,y)

# add() function:
print("sum of the arguments",operator.add(x,y))

# sub() function:
print("subtraction of the arguments",operator.sub(x,y))

# mul() function:
print("multiplication of the arguments",operator.mul(x,y))

# truediv() function:
print("division of the arguments",operator.truediv(x,y))

# floordiv() function:
print("floor division of the arguments",operator.floordiv(x,y))

# Pow() function:
print("exponentiation of the arguments",operator.pow(x,y))

# mod() function:
print("mod of the arguments",operator.mod(x,y))

# le() function:
print(" a is less than or equal b:",operator.le(x,y))

# lt() function:
print(" a is less than b:",operator.le(x,y))

# eq() function:
print(" a is equal to b:",operator.le(x,y))







