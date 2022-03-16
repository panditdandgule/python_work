import random


class Employee:
    count = 100
    ROLE_LIST = ['SE', 'SSE', 'MANAGER', 'LEAD', 'TEST ENGINEER']
    DEPT_LIST = ['HR', 'DEV', 'TEST', 'JAVA', 'PYTHON']

    def __init__(self, eid, ename, eage, erole, esal, edept, eskill, gender, rating):
        self.empId = eid
        self.empName = ename
        self.empAge = eage
        self.empRole = erole
        self.empSalary = esal
        self.empDept = edept
        self.empSkill = eskill
        self.empGender = gender
        self.empRating = rating

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    @classmethod
    def get_employee_instance(cls):
        role = cls.ROLE_LIST[random.randint(0, len(cls.ROLE_LIST) - 1)]
        dept = cls.DEPT_LIST[random.randint(0, len(cls.DEPT_LIST) - 1)]
        cls.count += 1

        skills = [chr(random.randint(65, 90)) for item in range(random.randint(2, 10))]

        gender = random.randint(0, 1)  # 0 - Male -->1 Female
        rating = [random.randint(1, 10) for item in range(3)]

        return cls(eid=cls.count, ename='AAAA' + str(cls.count), eage=random.randint(21, 45),
                   erole=role, esal=random.randint(10000, 50000), edept=dept,
                   eskill=skills,
                   gender=gender,
                   rating=rating)
