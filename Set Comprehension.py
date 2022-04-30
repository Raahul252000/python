# Set comprehensions are pretty similar to list comprehensions. The only difference between them is that
# set comprehensions use curly brackets { }.
# syntax:{expression for in iterable if conditional}

list1 =[2,3,42,3,54,25,3,3,5,21,2,44,44,54,21]
set1 = set()
for item in list1:
    set1.add(item*item)
print("before using set comprehension:",set1)

set2 = {item*item for item in list1}
print("after using set comprehension:",set2)