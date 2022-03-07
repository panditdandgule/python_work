def decorator(funcref):


    def inner(name):
        print("**"*40)
        print("Decorator started..")
        print("Welcome to Python "+funcref(name))
        print("Decorator completed..")
        print("**"*40)
    return inner


@decorator
def welcome(name):
    return name

welcome("Pandit")
