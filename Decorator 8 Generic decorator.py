"""
general decorator function is a type of decorator which can be used on multiple function.
"""
def division_deco(func):
    def inner(*args):                 # passing args in the inner function because different function could have different numbers of arguments.
        list1 = args[1:]
        for i in list1:
            if i == 0:
                return "divisor can't be zero."
        result = func(*args)
        return result
    return inner

@division_deco
def div1(a,b):
    return a/b

@division_deco
def div2(a,b,c):
    return a/b/c

print(div1(76,4))
print(div2(8,9,0))