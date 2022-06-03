"""
Any callable python object that is used t0 modify a function or a class is called as Decorator.
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
"""
#PASSING FUNCTION AS AN ARGUMENT.
# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(fun):
#     result = fun("heLLo there!!! How can i help you.")
#     print(result)
#
# greet(whisper)
# greet(shout)

# Example 1:
import time
def dec1(fun):
    def time1(msg):
        start = time.time()
        time.sleep(7.6)
        print(start)
        fun(msg)
        print(time.time()-start)
    return time1
@dec1
def greet(msg):
    print(msg)
greet("This is rahul yadav.")
