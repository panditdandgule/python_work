"""
We can define multiple decorators for the same function and all these decorators will
form decorator chaning.
@decor1
@decor2at
def num():
   for num() function we are applying 2 decorator functions.
   first inner decorator will work and then outer decorator.

"""

def decor1(func):
    def inner_func():
        x=func()
        return x*x
    return inner_func

def decor(func):
    def inner_func():
        x=func()
        return 2*x
    return inner_func

@decor1
@decor
def num():
    return 10

print(num())