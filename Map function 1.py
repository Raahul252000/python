"""
map() function returns a map object(which is an iterator) of the results after applying the given function to
each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list),
 set() (to create a set) .

"""
# applying int function on every items of the list.
list1 = ["23","12","11","34"]
print(list1)
print(type(list1))
number = list(map(int,list1))
print(number)
print(type(number))

#  applying square function on every items of the list.
list2 = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda a: a*a,list2))
print(square)

def sq(a):
    return a*a

def cube(a):
    return a*a*a

func = [sq, cube]

for i in range(5):
    values = list(map(lambda x:x(i),func))
    print(values)

