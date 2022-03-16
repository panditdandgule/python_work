import pymysql

from empinfo import Employee
from dbconnection import get_connection


def take_user_inputs():
    empid = int(input("Enter Employee id: "))
    empname = input("Enter Employee Name: ")
    empage = int(input("Enter Employee Age: "))
    emprole = input("Enter Employee Designation: ")
    empsal = float(input("Enter Employee Salary: "))
    empdept = input("Enter Employee Department: ")
    empskill = input("Enter employee skill:")
    empgender = input("Enter Employee Gender: ")
    emprating = int(input("Enter Employee Rating: "))
    return Employee(empid, empname, empage, emprole, empsal, empdept, empskill, empgender, emprating)


def create_employee_info():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        empinfo = take_user_inputs()
        query = "insert into employee values(%d,'%s',%d,'%s',%f,'%s','%s','%s',%d)";
        cursor.execute(query % (
        empinfo.empId, empinfo.empName, empinfo.empAge, empinfo.empRole, empinfo.empSal, empinfo.empDept,
        empinfo.empSkill, empinfo.empGender, empinfo.empRating))
        conn.commit()
        print("Data saved successfully..")
    except pymysql.DatabaseError as e:
        if conn:
            conn.rollback()
        print("There was an error connecting database", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    create_employee_info()
