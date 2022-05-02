"""
Python Coroutine:

In Python, coroutines are similar to generators but with few extra methods and slight changes in how we use
yield statements. Generators produce data for iteration while coroutines can also consume data.
In Python 2.5, a slight modification to the yield statement was introduced, now yield can also be used as an expression.
For example on the right side of the assignment –

line = (yield)
whatever value we send to coroutine is captured and returned by (yield) expression.

A value can be sent to the coroutine by send() method. For example, consider this coroutine which prints out the name
having the prefix “Dear” in it. We will send names to coroutine using send() method.

Execution of Coroutine:

The execution of the coroutine is similar to the generator. When we call coroutine nothing happens, it runs only
in response to the next() and sends () method. This can be seen clearly in the above example, as only after
calling __next__() method, our coroutine starts executing. After this call, execution advances to the first yield
expression, now execution pauses and waits for the value to be sent to instance object. When the first value is sent to it,
it checks for prefix and print name if prefix present. After printing the name, it goes through the loop until
it encounters the name = (yield) expression again.

"""
# Example 1:
def findtext():
    import time
    print("Function is under execution.")
    book = "this is the book about python, which will teach your everything about it and make you master at it."
    time.sleep(5)
    while (True):
        text = (yield)
        if text in book:
            print("yes text is in there.")

        else:
            print("no, there is nothing like that.")

search = findtext()
search.__next__()
search.send("python")
search.send("this is the")
search.send("this is the rahul")

#search.close()
search.send("python")


# Example 2:
def searchdata():
    import time
    print("function is under execution...")
    data = [12,21,11,34,3,13,15,67,76,34,22,25,7,6,8,]
    time.sleep(5)
    while (True):
        num = (yield)
        if num in data:
            print("yes data there in the list.")
        else:
            print("no data is not there in the list.")

search = searchdata()
search.__next__()
search.send(34)