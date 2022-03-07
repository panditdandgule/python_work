from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def inner_func(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        print("Executation time",end-start)
        return result
    return inner_func

@time_it
def substraction_of_numbers(*args):
    total=1000
    for val in args:
        total-=val
    return total

print("Substraction of Numbers: ",substraction_of_numbers(10,20,30))

