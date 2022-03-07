from impl import EmployeeServicesImpl
from empinfo import Employee

import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("New request came")

def get_user_inputs():
    try:
        empid=int(input("Enter Employee Id: "))
        empname=input("Enter Employee Name: ")
        empage=int(input("Enter Employee Age: "))
        empsalary=float(input("Enter Employee Salary: "))
        empaddress=input("Enter employee address: ")
        logging.info("Process completed successfully..")
        return Employee(empid,empname,empage,empsalary,empaddress)
    except ValueError as e:
        logging.exception(e)
    except:
        print("Invalid input..")

if __name__=='__main__':
    empobj=EmployeeServicesImpl()

    #empdetails=get_user_inputs()
    #empobj.add_employee_details(empdetails)

    empobj.display_employee_details()

    #empobj.search_employee_details()

    empobj.update_employee_details()

    #empobj.delete_employee_details()
