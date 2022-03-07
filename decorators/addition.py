import time

def time_it(funcref):
    def inner(x,y):
        start=time.time()
        funcref(x,y)
        time.sleep(1)
        end=time.time()
        print("Total time: ",end-start)
    return inner

@time_it
def add_two_numbers(x,y):
    sum=0
    sum=x+y
    print("Total Sum: ",sum)
    return sum

add_two_numbers(50,20)

