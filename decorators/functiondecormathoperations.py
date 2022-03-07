import time


def validate_integer(funcref):
    def inner_function(*args):
        flag = True
        for val in args:
            if type(val) == int:
                flag = True
            else:
                flag = False
                break
        if flag:
            return funcref(*args)
        else:
            print("Invalid Input!")

    return inner_function


def print_star(funcref):
    def inner_function(*args):
        print("**" * 40)
        y = funcref(*args)
        print("**" * 40)
        return y

    return inner_function


def time_it(funcref):
    def inner_function(*args):
        start_time = time.time()
        x = funcref(*args)
        end_time = time.time()
        print("Total time: ", end_time - start_time)
        return x

    return inner_function


@validate_integer
@time_it
@print_star
def add_numbers(*args):
    total = 0
    for val in args:
        total += val
    return total


@validate_integer
@time_it
@print_star
def substract_number(*args):
    total = 100
    for val in args:
        total -= val
        time.sleep(1)
    return total


@validate_integer
@time_it
@print_star
def multiply_number(*args):
    total = 1
    for val in args:
        total *= val
    return total


@validate_integer
@time_it
@print_star
def division_number(*args):
    total = 1
    for val in args:
        total += val
    return total / len(args)


print("Addition Of Numbers: ", add_numbers(10, 20, 30))
print("Subtraction Of Numbers: ", substract_number(40, 20, 10))
print("Multiplication Of Numbers: ", multiply_number(10, 20, 5, 2, 4))
print("Division Of Numbers: ", division_number(10, 4, 5, 6, 2))
