# Example 3:

import time
def get_time(fun):
    def get_timenow(numbers):
        initial_time = time.time()
        result = fun(numbers)
        print(result)
        execution_time = time.time()-initial_time
        print("time taken by the function ",execution_time)
        return result
    return get_timenow
@get_time
def cal_square(numbers):
    result1 = []
    for i in numbers:
        result1.append(i*i)
    return result1
@get_time
def cal_cube(numbers):
    result1 = []
    for i in numbers:
        result1.append(i*i*i)
    return result1

array = range(1,100)
cal_cube(array)
# cal_square(array)