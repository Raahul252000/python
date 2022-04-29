# Iteration with while loop:
list1 = [5,2.4,"rahul",44,23]
for item in list1:
    print(item)

for i in "this is rahul.":
    print(i)
# what is Iteration?: the process of traveling from one element to another is known as Itration.
# with for loop we can travel through every elements in strings,list,tuple,dictionary and set.

               # Q: what if in some conditons we are not allowed to use the for loop?
               # Ans: then we can use the while loop, but the while loop only works on those indexed objects like
               #      list,tuple and strings. while loop doesn't work for sets and dictionary because they are not indexed.

# Iteration with while loop:
fruits = ["apple",12,"orange","grapes",1]
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1


st = "this is the best thing."
j = 0
while j < len(st):
    print(st[j])
    j+=1

# apart from for loop, to travel through all the elements of the sequence(tuple,string list),set and dictionary,
# we can use another method called as ITERATOR PROTOCALL.
# ITERATOR PROTOCALL: the way of working with iterators and iterable.
# ITERABLE: everything we can loop over is known as iterables. examples are string,list,tuple,set and dictionary.
# all the ITERABLES objects such as sequence(tuple,string and list),set and dictionary call the built-in function "iter"
# which will give ITERATORS as output  and that iterator will give the next elements of the Iterables.

# example 1:
list2 = ["rahul",33,"abc",11]
#print(iter(list2))
iterator = (iter(list2))             # iter() function will return the iterator object.
print(next(iterator))                # next() function will return the next element.
print(next(iterator))
print(next(iterator))
print(next(iterator))

# example 2:
color = ["red","orange","green"]
def print_each(list):
    iterator1 = iter(list)
    while True:
        try:
            items = next(iterator1)
        except StopIteration:
            break
        else:
            print(items)

print_each(color)


