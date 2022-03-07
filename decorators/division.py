from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def inner_function(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("Execuation Time: ", end - start)
        return result

    return inner_function


@time_it
def division_of_numbers(*args):
    total = 0
    for val in args:
        total += val
        time.sleep(1)
    return total / len(args)


print("Total Divion Number: ", division_of_numbers(10, 20, 40, 50))
