"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:

filter(function, sequence)

Parameters:
function: function that tests if each element of a
sequence true or not.
sequence: sequence which needs to be filtered, it can
be sets, lists, tuples, or containers of any iterators.

Returns:
returns an iterator that is already filtered.
"""
# filtering the number smaller than 11:
list1 = [24,25,1,5,12,13,56,6,9,10,22]

def great_5(num):
    return num>11

filtered = list(filter(great_5,list1))
print(filtered)


#filtering consonant :
def che_vowles(var):
    vowels = ["a","e","i","o","u"]
    if var in vowels:
        return True
    else:
        False

seq = ["a","b","c","d","e","f","g","h","i","j","k"]

filtered = list(filter(che_vowles,seq))
print(filtered)


#
list2 = [2,3,4,6,7,8,12,13,14,16]
# filtering even number from the list:
result = list(filter(lambda x: x%2 != 0,list2))
print(result)


# filtering odd number from the list:
result = list(filter(lambda x: x%2 ==0,list2))
print(result)