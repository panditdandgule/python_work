from studaddress import Address
class Department(Address):
    def __init__(self,dnm,did,city,state,country):
        super(Department, self).__init__(city,state,country)
        self.deptName=dnm
        self.deptId=did

    def display_stud_info(self):
        super(Department, self).display_stud_info()
        print("Student Department Name: ",self.deptName)
        print("Student Department Id: ",self.deptId)


    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''
