def decorator_func(funcref):

    def inner_func(*args):
        print("Befor decroator")
        print("Total",funcref(*args))
        print("after decorator")

    return inner_func

#decorator_func(add_func())
@decorator_func
def add_func(*args):
    total=0
    for x in args:
        total+=x

    return total

add_func(10,20,30)