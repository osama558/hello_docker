import pymysql 
import sqlite3

class db():
# Connect to the database
    def __init__(self):
        pass
    def connection():
        connectionn = pymysql.connect(host='db4free.net',
                                    user='osamadatabase',
                                    port=3306,
                                    password='-J5Mvgmk_uzE*ZU',
                                    database='databaseosama',
                                    cursorclass=pymysql.cursors.DictCursor)
        #print('Connected')
        return connectionn
    def insert_record(name,number):
        conn = db.connection()
        with conn:
            with conn.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO test (name, number) VALUES (%s, %s)"
                cursor.execute(sql, (str(name), number))
                conn.commit()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
                
    def read():
        with db.connection().cursor() as cursor:
            # Read a single record
            sql = "SELECT * from test"
            cursor.execute(sql)
            result = cursor.fetchall()
            #print(result)
        # df = pd.DataFrame(result)
        # df.to_csv("dataframe.csv")
        # with open("dataframe.txt", "w") as file1:
        #     for i in result:
        #         print(i)    
        #         file1.write(str(i)+'\n')
        #     file1.close()
        return result


#db.insert_record("gg",66)
#db.read()

# Driver Code 
#if __name__ == "__main__" : 
#    mysqlconnect()