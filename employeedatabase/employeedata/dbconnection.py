import pymysql

def get_connection():
    try:
        connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   port=3305,
                                   database='employeedata')
        return connection
    except pymysql.DatabaseError as e:
        print("There was problem with sql",e)
