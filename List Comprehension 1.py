"""
One of the most distinctive aspects of the language is the python list and the list compression feature,
which one can use within a single line of code to construct powerful functionality.

List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
A list comprehension consists of brackets containing the expression, which is executed for each element along with
the for loop to iterate over each element.

Syntax:
[expression for item in iterable]
            Or
[expression for iten in iterable if conditonl]
            Or
[expression if conditional else stmnt for item in iterable]
note 1: list comprehension is used when we have to apply any operation on every element of list.
note 2: list comprehension is a very good substitute for map,filter and reduce function.
"""
# Example 1:
# traditionl way of making list with for loop.
list1 = []
for i in range(1,100):
    if i%2 == 0:
        list1.append(i)
print(list1)

# new way of doing same thing with list comprehension:
list2 = [i for i in range(1,50) if i%2==0]      # in one line
print(list2)

# Example 2:
list3 = [x if x>2 else x+1 for x in range(1,11)]
print(list3)

# Example 3:
listl4 = [1,2,3,4,5]
print(f"before list comprehension: {listl4}")
listl4 = [x*10 for x in listl4]
print(f"after list comprehension: {listl4}")

# Example 4: change the case of the letters.
words = ["hello","to","everyone"]
print(f"after list comprehension: {words}")
words = [item.upper() for item in words ]
print(f"after list comprehension: {words}")

# Example 5: Extracting numbers from string.
str = "thisisrahul252000"
str = [x for x in str if x.isdigit()]
print(str)

# Example 6: Extracting alphabets from string.
str = "thisisrahul252000"
str = [x for x in str if x.isalpha()]
print(str)

# Example 7: extracting first element form nested list
list5 = [[1,2,3],[4,5,6],['a','b']]
list5 = [x[0] for x in list5]
print(list5)

# Example 8: list comprehension on function:
def square(x):
    return x*x
sq = [square(x) for x in range(1,11)]
print(sq)

# Example 9: adding elements of two list
a = [1,2,3,4,5]
b = [12,13,14]
add = [x+y for x in a for y in b]
print(add)

