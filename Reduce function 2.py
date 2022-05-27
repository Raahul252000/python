import functools
list1 = [22,12,1,5,9,32,21,14,19,47]
# highest number of the list:
result = functools.reduce(lambda a,b: a if a>b else b,list1)
print("largest number of the list:",result)

# smallest number of the list:
result1 = functools.reduce(lambda a,b: a if a<b else b,list1)
print("smallest number of the list:",result1)

# adding all the elements of the list:
list_sum = functools.reduce(lambda a,b: a+b,list1)
print("sum of all the elements of the list: ",list_sum)

# multiplication of all the elements of the list:
list_multi = functools.reduce(lambda a,b: a*b,list1)
print("multiplication of the elements of the list:",list_multi)
