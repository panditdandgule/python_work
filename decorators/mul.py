from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def inner_func(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        print("Execuation Time: ",end-start)
        return result
    return inner_func

@time_it
def multiplication_of_numbers(*args):
    total=1
    for val in args:
        total*=val
    time.sleep(2)
    return total

print("Multiplication Of Numbers: ",multiplication_of_numbers(10,20,30))