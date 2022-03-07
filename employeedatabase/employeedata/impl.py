import pymysql

from employeeservices import EmployeeServices, Employee
from employeedata import dbconnection


class EmployeeServicesImpl(EmployeeServices):

    def add_employee_details(self, empdetails):
        try:
            conn = dbconnection.get_connection()
            cursor = conn.cursor()
            sql = "insert into employee values(%d,'%s',%d,%f,'%s')"
            cursor.execute(sql % (
            empdetails.empId, empdetails.empName, empdetails.empAge, empdetails.empSalary, empdetails.empAddr))
            conn.commit()
            print("Data Added susccessfully..")
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def display_employee_details(self):
        try:
            conn=dbconnection.get_connection()
            cursor=conn.cursor()
            cursor.execute("select *from employee")

            data=cursor.fetchall()
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
        else:
            for row in data:
                print(row)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def search_employee_details(self):
        empid=int(input("Enter which id you want to search ? "))
        try:
            conn=dbconnection.get_connection()
            cursor=conn.cursor()

            sql="select * from employee where empid=%d"
            cursor.execute(sql %(empid))
            data=cursor.fetchone()
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
        else:
            print("================================================================")
            print("ID\t\tName\t\t\tAge\t\t\tSalary\t\t\tAddress")
            print("================================================================")
            print(data[0],"\t\t",data[1],"\t\t",data[2],"\t\t",data[3],"\t\t",data[4])
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_employee_details(self):
        empid=int(input("Enter which id you want to update? "))

        try:
            conn=dbconnection.get_connection()
            cursor=conn.cursor()
            sql="select * from employee where empid=%d"
            cursor.execute(sql %(empid))

        except:
            pass
        else:
            confirm=input("Do you want to update this id? (y|n): ")
            if confirm.lower()=='y':

                empname=input("Enter Name: ")
                age=input("Enter Age: ")
                salary=float(input("Enter Salary: "))
                address=input("Enter Address: ")
                sql="update employee set empname='%s',age=%d,salary=%f,address='%s' where empid=%d"
                cursor.execute(sql %(empname,age,salary,address,empid))
                conn.commit()
                print("Data updated successfully.")
            else:
                print("invalid input")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delete_employee_details(self):
        empid=int(input("Enter id which one you want to delete? "))
        try:
            conn=dbconnection.get_connection()
            cursor=conn.cursor()
            sql="select *from employee where empId=%d"
            cursor.execute(sql %(empid))



        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
        else:
            print(cursor.fetchone())
            confirm=input("Do you want to delete this (y|n): ")
            sql="delete  from employee where empid=%d"
            if confirm.lower()=='y':
                cursor.execute(sql %(empid))
                conn.commit()
                print("Deleted successfully..")
            else:
                print("Invalid input..")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
