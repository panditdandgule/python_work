from functools import wraps

def print_star(func):
    @wraps(func)
    def inner_func(*args):
        print("++"*40)
        result=func(*args)
        print(func.__name__)
        print(result)


    return inner_func

@print_star
def addition_numbers(*args):
    total=0
    for val in args:
        total+=val
    return (args,"Addition Of Numbers",total)

@print_star
def substarct_numbers(*args):
    total=100
    for val in args:
        total-=val
    return (args,"Substraction Of Numbers: ",total)

addition_numbers(10,20,30,40,50)
substarct_numbers(10,20,30,50,54)