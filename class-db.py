## INSTAL PIP
## pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print('CON SUCCESS')
    except Error as e:
        print(f'The Error {e} occurred')
    return connection
conn = create_con('cis3368spring.c1k04kwms2vg.us-east-1.rds.amazonaws.com', 'admin', 'PerlaDBCIS3368', 'cis3368springDB')
cursor = conn.cursor(dictionary = True)
sql = 'SELECT * FROM users'
cursor.execute(sql)
rows = cursor.fetchall()

for user in rows:
    print(user)
    print('first name is:' + user['firstname'])
    fname = user['firstname']