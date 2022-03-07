class Employee:
    def __init__(self,eid,ename,eage,esal,eaddr):
        self.empId=eid
        self.empName=ename
        self.empAge=eage
        self.empSalary=esal
        self.empAddr=eaddr

    def __str__(self):
        return f'''\n{self.__dict__}\n'''

    def __repr__(self):
        return str(self)

