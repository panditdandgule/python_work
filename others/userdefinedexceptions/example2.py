class ZeroDivision(Exception):
    def __init__(self,arg):
        self.msg=arg

class DivisionExample:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def divide_two_numbers(self):
        try:
            return self.x/self.y
            raise ZeroDivision("Can not divide with zero")
        except ZeroDivision as err:
            print(err.msg)



d=DivisionExample(10,5)
print(d.divide_two_numbers())