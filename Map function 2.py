# Example 1: double the element.
def addition(num):
    return num+num
numbers = (1,2,3,4,5)
result = list(map(addition,numbers))
print(result)

# we can achieve the same result with the help of lambda and map function:
numbers = (1,2,3,4,5)
result1 = list(map(lambda x: x+x,numbers))
print("with the help of lambda and map function:",result1)

# Example 2: changing the name in upper case:
animals = ["dog","cat","giraffe","lion","monkey","tiger","bear"]
uppercase = list(map(lambda name: str(name).upper(),animals))
print(uppercase)
