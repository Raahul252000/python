"""
What is the Enumerate Function in Python?
The enumerate() function in Python takes in a data collection as a parameter and returns an enumerate object.
The enumerate object is returned in a key-value pair format. The key is the corresponding index of each item and the
value is the items.

syntax: enumerate(iterable, start)

The enumerate() function takes in two parameters: iterable and start.

1.Iterable is the data collection passed in to be returned as an enumerate object.
2.start is the starting index for the enumerate object. The default value is 0 so if you omit this parameter, 0 will be
used as the first index.
"""

# example 1: get enumerate object.
list1 = ["rahul","amit","tina","isha"]
e = list(enumerate(list1))    # a is enumerate object.
print(e)

# example 2: print the index and value at that index
list2 = ["a","b","c","d"]
for index, value in enumerate(list2):
    print(value,index)

# example 3: print the value of even indices.
print("even indices and their value:")
list3 = [1,2,3,4,5,6,7,8,9,10]
for index, value in enumerate(list3):
    if index%2==0:
        print(value,index)

#
list4 = [45,56,76,86,96,106]
for value in enumerate(list4):
    print(value)