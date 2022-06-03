# Example 5: sum from zero to the given number from the user:

from time import time
def decfun(func):
    def inner(num):
        start = time()
        result1 = func(num)
        end = time()
        print(f" it took {end-start} to complete the task.")
        return result1
    return inner

@decfun
def summ(num):
    result = sum([i for i in range(num+1)])
    return result

print(summ(20000000))