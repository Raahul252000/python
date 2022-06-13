"""
when we
"""
import random

# random(): generates floating value between 0 and 1 (including 0 but excluding 1). It does not require any arguments.
print(random.random())
print(random.random())

# randrange(start,stop,step): This method always returns an interger between given lower and upper limit to this method (excluding upper limit.)
print(random.randrange(4,20,2))

# randint(a,b): It will generate random integer values within the range a to b (including a and b both), where a must be less than or equal to b.
a = random.randint(2,8)
print(a)

# uniform(a,b): Returns any floating point number between two given numbers.
a = random.uniform(2,5)
print(a)
print(random.uniform(2,5))

# choice(sequence): This method chooses randomly from the given sequence.
list = [44,55,66,20]
print(random.choice(list))

list1 = ["a","b","c","d"]
print(random.choice(list1))

# shuffle(sequence): This method shuffle the items of the given list.
random.shuffle(list)
print(list)