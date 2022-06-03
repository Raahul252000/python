# Example 4:

def decoratorfun(func):
    def inner(x,y):
        print("divide",x,"and",y)
        if y == 0:
            print("division with zero is not allowed.")
            return
        else:
            result = func(x,y)
            return result
    return inner

@decoratorfun
def divide(a,b):
    return a/b

print(divide(34,0))