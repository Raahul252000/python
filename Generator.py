# Generator function: it is a function which returns generator-iterator with the help of 'yield' keyword.
# generator iterator is nothing but special type of iterators, all generator-iterators is a iterator but all iterator
# are not generator iterator.
# If the body of a def contains yield, the function automatically becomes a generator function.

def fib(num):
    a,b = 0,1
    while True:
        c = a+b
        if c<num:
            print("before yield keyword")
            yield c
            print("after yield keyword")
            a = b
            b = c
        else:
            break

gen = fib(15)
print(gen.__next__())
print(gen.__next__())
print(next(gen))
print(next(gen))
print(gen.__next__())
print(gen.__next__())
print(next(gen))
