class MyError(Exception):
    def __init__(self,arg):
        self.msg=arg

    def __str__(self):
        return f'''{self.msg}'''