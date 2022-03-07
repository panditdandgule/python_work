import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        #Do something before
        value=func(*args,**kwargs)
        #Do something after
        return value
    return wrapper_decorator

@decorator
def func_new(*args,**kwargs):
    for val in args:
        print(val)
    print("Welcome")
    for k,v in kwargs:
        print(k,v)

func_new(10,20,{'key':'value'})
