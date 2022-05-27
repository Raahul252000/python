"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
mentioned in the sequence passed along.This function is defined in “functools” module.

Working :

1.At first step, first two elements of sequence are picked and the result is obtained.
2.Next step is to apply the same function to the previously attained result and the number just succeeding the second
element and the result is again stored.
3.This process continues till no more elements are left in the container.
4.The final returned result is returned and printed on console.
"""

list1 = [1, 2, 3, 4, 5, 6]
# old method to add all the items of the list:

# sum = 0
# for item in list1:
#     sum = sum + item
# print(sum)

# adding all the item of the list with reduce() function:

from functools import reduce

sum1 = int(reduce(lambda x, y: x + y, list1))
print(sum1)

# multiplication of all the item of the given list.

multi = reduce(lambda x,y: x*y,list1)
print(multi)
