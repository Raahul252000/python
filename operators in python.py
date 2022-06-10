""" Arithmetic operators"""
a = 5
b = 10
c = 2
d = 3
print(a+b)
print(c**d)
print(d**a)         # ** is used for exponential.
print(b/a)
print(b%d)          # % (modulus) is used to get remainder.
print(b*a)          # * for multiplication.
print(b/d)
print(b//d)         #the floor division // rounds the result down to the nearest whole number


# Assignment operators.
a +=a
print(a)
d **= d
print(d)
c *= c
print(c)
a /= a
print(a)


# Membership Operators:
lis = ["python", "Java", "Html", 12, 34, 5]
print("python" in lis)
print(23 in lis)
print("java" in lis)
print("Java" in lis)
print("tina" in lis)
print("Html" not in lis)
print("tina" not in lis)

# Identity operators:
lis1 = ["python", "Java", "Html", 12, 34, 5]
x = lis1
print( a is a)
print(a is b)
print(lis is lis1)
print(lis1 is x)
print(lis1 is not a)
print(lis1 is not x)

