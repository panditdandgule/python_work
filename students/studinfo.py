from deptinfo import Department

class Student(Department):
    def __init__(self,sid,snm,sage,sph,dnm,did,city,state,country):
        super(Student, self).__init__(dnm,did,city,state,country)
        self.studId=sid
        self.studName=snm
        self.studAge=sage
        self.studPhone=sph

    def display_stud_info(self):
        print("Student Id: ",self.studId)
        print("Student Name: ",self.studName)
        print("Student Age: ",self.studAge)
        print("Student Phone: ",self.studPhone)
        super(Student, self).display_stud_info()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''



studentsList=[]

n=int(input("Enter number of students: "))
for x in range(n):
    studId=int(input("Enter student id: "))
    studName=input("Enter student name: ")
    studAge=int(input("Enter Student Age: "))
    studPhone=int(input("Enter student phone number: "))
    deptName=input("Enter department name: ")
    deptId=int(input("Enter department id: "))
    city=input("Enter city name: ")
    state=input("Enter state name: ")
    country=input("Enter country name: ")

    s=Student(sid=studId,snm=studName,sage=studAge,sph=studPhone,dnm=deptName,did=deptId,city=city,state=state,country=country)
    studentsList.append(s)

for stud in studentsList:
    print(stud)