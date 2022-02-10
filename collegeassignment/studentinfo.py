from addressinfo import Address
from deptinfo import Department


class Student:
    '''This structure is defined  for student to hold data and properties'''
    collegeName = 'Modern College,Pune'

    def __init__(self, sid, sname, sage, semail, dept: Department, addr: Address):
        self.studId = sid
        self.studName = sname
        self.studAge = sage
        self.studEmail = semail
        self.studDept = dept
        self.studAddr = addr

    def __str__(self):
        return """{} {} {} {} {} {}\n""".format(self.studId,
                                              self.studName,
                                              self.studAge,
                                              self.studEmail,
                                              self.studDept,
                                              self.studAddr)

    def __repr__(self):
        return str(self)
