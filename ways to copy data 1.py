# shallow copy:
"""
There are various way to copy:
1. built-in functions: list(),set(),dict()
2. slicing operator
3. list comprehension
4. copy function copy module.
"""

# by using built-in function:
list1 = [2,1,4,5]
list2 = list(list1)
print(list2)
list2.append("rahul")
print(list2)
print(list1)

# using slicing operator:
lis1 = [11,22,33,44]
lis2 = lis1[:]
print(lis2)
lis2[0] = "anil"
print(lis2)
print(lis1)

# using list comprehension:
list_a = [100,200,300,400]
list_b = [x for x in list_a]
print(list_b)
list_b[2] = "chhota don"
print(list_b)
print(list_a)

# using copy module:
from copy import copy
list_x = ["a","b","c","d"]
list_y = copy(list_x)
print(list_y)
list_y[-1] = "chota chatri"
print(list_y)
print(list_x)
print(id(list_x) == id(list_y))    # id is different it means both are different objects

"""
Note: In the case of compound object or nest list, nested dictionary, we dont use shallow copy.
we use deepcopy, because after doing shallow copy if we try to modify the any nested list or compound object, it affects
both the list means it modifies both the nested list.
"""