from empinfo import  Employee

class EmployeeImpl:
    filename='employee.csv'

    def add_employee_info(self,edetails):

        try:
            empinfo=str(edetails.eid)+","+edetails.ename+","+edetails.eadr+"\n"
            with open(self.filename,'w') as f:
                f.writelines(empinfo)
                print("data written successfully")
        except:
            print("There was an error while adding data")


    def read_employee_info(self):
        try:
            newList=[]
            with open(self.filename,'r') as f:
                alllines=f.readlines()
                alllines=[line.strip() for line in alllines]

                for line in alllines:

                    words=line.split(',')
                   
                    newList.append(Employee(eid=words[0],ename=words[1],eadr=words[2]))
            print("All student list: ",newList)

        except:
            print("There was an error while reading csv file.")