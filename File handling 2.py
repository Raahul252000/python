"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
# Example 1:
try:
    for i in range():
        print(i)
except Exception as e:
    print(e)

name = "this is rahul."
list1 = [i for i in name]
print(list1)


# Example 2:
f = open("masti.txt","r")
try:
    f1 = open("thisismy.txt")
    print(f1.read())

except Exception as e:
    print(e)

finally:
    f.close()
    f1.close()
    list2 = [x**2 for x in range(1,11)]
    print(list2)

# Example 3:
print("Hello guy's....")
try:
    lis1 = [x**2 for x in range(1,15) if x%3 == 0]
    print(lis1)
except Exception as e:
    print(e)

else:
    print("try block worked properly.")

finally:
    print(" your code has no error.")