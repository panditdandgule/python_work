def smart_division(funcref):
    def inne_func(a,b):
        if b==0:
            print("OOPS b is zero..")
            return
        else:
             return funcref(a,b)
    return inne_func


@smart_division
def division_numbers(x,y):
    return x/y

print("Division of Numbers: ",division_numbers(10,20))
print("Division of Numbers: ",division_numbers(10,0))