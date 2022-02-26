import pymysql

try:
    con=pymysql.connect(host='localhost',
                        user='root',
                        password='root',
                        port=3305,
                        database='studinfo')

    cursor=con.cursor()
    sql="create table student(sid int primary key auto_increment,sname varchar(30),sage int,saddr varchar(30))";
    cursor.execute(sql)
    print("Table created successfully")
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There was error in database",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()