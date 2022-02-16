class YourException(Exception):
    def __init__(self,arg):
        self.msg=arg

try:
    raise YourException("Something wrong")
except YourException as err:
    print("Error",err.msg)