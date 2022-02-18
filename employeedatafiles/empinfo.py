class Employee:
    def __init__(self,eid,ename,eadr):
        self.eid=eid
        self.ename=ename
        self.eadr=eadr

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)