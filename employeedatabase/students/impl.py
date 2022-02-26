from studinfo import Student
import pymysql

class StudentImpl:

    def add_student_info(self,details):
        try:
            con=pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                port=3305,
                                database='studinfo')

            cursor=con.cursor()
            sql="insert into student values(%d,'%s',%d,'%s')"

            cursor.execute(sql %(details.studId,details.studName,details.studAge,details.studAddr))
            print("Record inserted successfully")
            con.commit()


        except pymysql.DatabaseError as e:
            if con:
                con.rollback()
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def display_student_info(self):
        try:
            con=pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                port=3305,
                                database='studinfo')
            cursor=con.cursor()
            cursor.execute("select *from student")
            data=cursor.fetchall()
            print("ID\t\tName\tAge\t\tCity")
            print("=========================")
            for row in data:
                print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])
            print("==========================")
        except pymysql.DatabaseError as e:
            if con:
                con.rollback()
                print("There was an problem with sql ",e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def update_student_info(self,id,name):
        try:
            con=pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                port=3305,
                                database='studinfo')
            cursor=con.cursor()
            sql="update student set sname=name where sid=id"
            cursor.execute(sql %(id,name))
            print("Record updated successfully..")
            con.commit()
        except pymysql.DatabaseError as e:
            if con:
                con.rollback()
                print("There was an error while updating data",e)
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()