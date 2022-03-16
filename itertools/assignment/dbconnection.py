import pymysql

def get_connection():
    try:
        connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   port=3305,
                                   database='iterassignment')
        #print("Database connection was successful..")

        return connection
    except pymysql.DatabaseError as e:
        if connection:
            connection.rollback()
        print("There was an error while connecting database.",e)
