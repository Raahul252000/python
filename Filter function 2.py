# Example 1: filtering vowels out.
def filter_vowels(var):
    vowels = ['a','e','i','o','u']
    if var in vowels:
        return True
    else:
        return False

letters = ['k','b','c','e','i','q','h','t','r','a','n','m']

filtered = list((filter(filter_vowels,letters)))                    # filter function takes function's name and iterable as arguments.
print(filtered)

# same question with the help of lambda function:
filtered = list(filter(lambda x: x in ['a','e','i','o','u'],letters))
print(f"filtered with the help of lambda and filter function: {filtered}")

# Example 2: filtering odd numbers:
list2 = [3,5,12,4,11,6,9,45,71,54,96,37]
filtered = list(filter(lambda x: x%2 != 0,list2))
print(filtered)


# Example 3: filtering age above 18:
ages = [12,67,45,17,21,14,89,76,7]
adults = list(filter(lambda x: x>18,ages))
print(adults)

# Example 5: one function can be returned from another function with bracket '()' also.

                        # returning function without bracket
def outer():
    x = 3
    def inner():
        y = 5
        result = x+y
        return result
    return inner

x = outer()
print(type(x))
print(x())


                          # returning function with bracket
def outer():
    x = 3
    def inner():
        y = 5
        result = x+y
        return result
    return inner()

y = outer()
print(y)
print(type(y))
