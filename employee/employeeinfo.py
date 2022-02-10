from emaddress import Address


class Employee:
    def __init__(self, empid, empnm, empage, empsal, empadr: Address):
        self.empId = empid
        self.empName = empnm
        self.empAge = empage
        self.empSalary = empsal
        self.empAdr = empadr

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''
