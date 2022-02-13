class Person:
    def __init__(self, pname, page):
        self.personName = pname
        self.personAge = page

    def display_info(self):
        print("Person Name: ", self.personName)
        print("Person Age: ", self.personAge)


class Employee(Person):
    def __init__(self, pname, page, empid, esalary):
        super(Employee, self).__init__(pname, page)
        self.empId = empid
        self.empSalary = esalary

    def display_info(self):
        super(Employee, self).display_info()
        print("Employee Id: ", self.empId)
        print("Employee Salary: ", self.empSalary)


class Dept(Employee):
    def __init__(self, pname, page, empid, esalary, depnm):
        super().__init__(pname, page, empid, esalary)
        self.depName = depnm

    def display_info(self):
        super(Dept, self).display_info()
        print("Department Name: ", self.depName)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''


personList=[]
n = int(input("Enter Number Of Employee: "))
for x in range(n):
    pname = input("Enter Person Name: ")
    page = int(input("Enter Person Age: "))
    empid = int(input("Enter Employee Id: "))
    esalary = float(input("Enter Employee Salary: "))
    deptnm = input("Enter Department Name: ")

    dept = Dept(pname, page, empid, esalary, deptnm)
    personList.append(dept)

print(personList)