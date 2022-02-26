class Student:
    def __init__(self,sid=None,sname=None,sage=None,saddr=None):
        self.studId=sid
        self.studName=sname
        self.studAge=sage
        self.studAddr=saddr

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

