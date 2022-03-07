import time


def print_star(funcref):
    def inner_func(*args):
        print("**" * 40)
        return funcref(*args)
        print("**" * 40)

    return inner_func


def validate_values(funcref):
    def inner_func(*args):
        flag = True
        for val in args:
            if type(val) == int:
                flag = True
            else:
                flag = False
                break
        try:
            if flag:
                return funcref(*args)
            else:
                print("Invalid Input!")
        except ValueError:
            return "Number required only integer.."

    return inner_func


def time_it(funcref):
    def innerfunc(*args):
        start_time = time.time()
        result = funcref(*args)
        end_time = time.time()
        print("Total time calculations: ", end_time - start_time)
        return result

    return innerfunc


@print_star
@validate_values  # validate_values(time_it(add_numbers()))
@time_it
def add_numbers(*args):
    total = 0
    for val in args:
        total = total + val
    return total


@print_star
@validate_values
@time_it
def substract_numbers(*args):
    total = 0
    for val in args:
        total = total - val
    return total


@print_star
@validate_values
@time_it
def multiply_numbers(*args):
    total = 1
    for val in args:
        total = total * val
    return total


@print_star
@validate_values
@time_it
def divide_numbers(*args):
    total = 0
    for val in args:
        total=total+val
    result = total / len(args)
    return result


print("Addition Of Numbers: ", add_numbers(10, 20, 30, 40))
print("Subtraction Of Numbers:", substract_numbers(20, 10, 5, 2))
print("Multiplication Of Numbers:", multiply_numbers(10, 20, 30, 40, 50))
print("Division Of Numbers: ", divide_numbers(5, 10, 20, 30, 40))
