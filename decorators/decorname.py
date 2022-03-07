def decor(funcref):
    def inner(name):
        if name=='Ravi':
            print("Hello",name,"Bad morning")
        else:
            funcref(name)
    return inner


@decor
def wish(name):
    print("Hello",name,"Good Morning")
    
wish("Pandit")
wish("Pratiksha")
wish("Ravi")

