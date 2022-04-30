# List comprehension is the best substitute for for-loop,map,filter and reduce function.
# Example 1:
# creating list with for loop:
list1 = []
for i in range(1,11):
    list1.append(i)
print(list1)

# replacing for-loop with list comprehension:
list1 = [i for i in range(1,11)]
print(list1)

# Example 2:
# using map function with lambda:
num = [1.2,2.3,4.5,6.1]
num = list(map(lambda x:int(x),num))
print(num)

# replacing map function with list comprehension:
num1 = [1.2,2.3,4.5,6.1]
num1 = [int(i) for i in num1]
print(num1)

# Example 3:
# using filter function for get list of even number between 1 to 11:
even = list(filter(lambda x:x%2 == 0,range(1,11)))
print(even)

# replacing filter function with list comprehension:
even = [x for x in range(1,11) if x%2==0]
print(even)

# using reduce function
from functools import reduce
summ= reduce(lambda x,y:x+y,[1,2,3,4])
print(summ)

# replacing reduce function with list comprehension:
sum1 = sum([x for x in [1,2,3,4]])
print(sum1)
