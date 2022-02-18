class Student:
    def __init__(self,sid,sname,sage,sadr):
        self.studId=sid
        self.studName=sname
        self.studAge=sage
        self.studAdr=sadr

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n{self.__dict__}\n'''
