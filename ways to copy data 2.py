# Deep copy
"""
Deepcopy: Creates a new objects and recursively adds the copies of nested objects present in the original elements.
To use deepcopy we need to import the copy module.
"""
from copy import deepcopy
list1 = [[100,200],10,20,30]
list2 = deepcopy(list1)

print(list2)
print(list1)

list2[0][1] = "chota don"

print(list2)
print(list1)

