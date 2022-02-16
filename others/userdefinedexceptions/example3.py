class MyError(Exception):
    def __init__(self,args):
        self.msg=args

    def __str__(self):
        return (repr(self.msg))


try:
    raise MyError(3*2)
except MyError as err:
    print('New exception occurred',err.msg)