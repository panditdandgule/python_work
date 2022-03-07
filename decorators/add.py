from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def inner_func(*args):
        start_time=time.time()
        result=func(*args)
        end_time=time.time()
        print("Execuation Time: ",end_time-start_time)
        return result
    return inner_func


@time_it
def addition_of_numbers(*args):
    total=0
    for val in args:
        total+=val
    time.sleep(1)
    return total


print("Addition: ",addition_of_numbers(10,30,40))