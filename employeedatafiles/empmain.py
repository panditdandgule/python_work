from imple import EmployeeImpl,Employee
import logging
logging.basicConfig(filename='myerror.log',level=logging.INFO)
logging.info("The new request came")

def take_user_inputs():
    try:
        eid=int(input("Enter employee id: "))
        ename=input("Enter employee name: ")
        eadr=input("Enter employee address")
        return Employee(eid,ename,eadr)

    except ValueError as msg:
        logging.exception(msg)
    except:
        print("Invalid input..")


if __name__=='__main__':
    emp=EmployeeImpl()

    #edetails=take_user_inputs()
    #emp.add_employee_info(edetails)

    emp.read_employee_info()