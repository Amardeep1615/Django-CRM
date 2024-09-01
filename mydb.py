#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import MySQLdb

try:
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        password="Amar!@#123",
        database="rama"
        
    )
    print("Connection successful")
    # Add your database operations here
except MySQLdb.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed")
