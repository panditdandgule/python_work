import operator

def myFunc(a,b,operation):
    return operation(a,b)

print("Addition: ",myFunc(2,3,operator.add))

print("Multiplication: ",myFunc(2,3,operator.mul))

for item in [operator.add,operator.mul,operator.sub,operator.truediv]:
    print(myFunc(2,3,item))

print(operator.add([2,3,4],[2,3,4]))