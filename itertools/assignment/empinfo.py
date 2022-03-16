class Employee:
    def __init__(self, eid, ename, eage, erole, esal, edept, eskill, egender, erating):
        self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empRole = erole
        self.empSal = esal
        self.empDept = edept
        self.empSkill = eskill
        self.empGender = egender
        self.empRating = erating

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)
