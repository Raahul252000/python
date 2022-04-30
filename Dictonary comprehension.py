# Dictionary comprehension: Extending the idea of list comprehensions, we can also create a dictionary using dictionary
# comprehensions. The basic structure of a dictionary comprehension looks like below.

# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

# Example 1:
# getting the square of item of list into dictionary by using for loop
dict1 = {}
list1 = [1,2,3,4,5]
for item in list1:
    dict1.update({item:item*item})
print(f"before using dictionary comprehension:{dict1}")

# substituting for loop by dictionary comprehension
list1 = [1,2,3,4,5]
dict2 = {item:item**2 for item in list1}
print(f"after using dictionary comprehension:{dict2}")

# Example 2:
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

# using for loop:
dict1 = {}
for key,value in zip(state,capital):
    dict1.update({key:value})
print("by using simple for loop: ",dict1)

# using dictionary comprehension:
dict1 = {key:value for key,value in zip(state,capital)}
print("by using dictionary comprehension: ",dict1)

