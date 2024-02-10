## INSTAL PIP
## pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname
            user = username
            password = userpw
            database = dbname
        )
        print('CON SUCCESS')
    except: Error as 0:
        print(f'The Error {e} occurred')
    return connection
conn = create_con('ENTER HOSTNAME HERE', 'admin', 'ENTER DB PW', 'ENTER DBNAME')
cursor = conn.cursor(dictionary = True)
sql = 'SELECT * FROM users'
cursor.execute(sql)
rows = cursor.fetchall()

for user in rows:
    print(user)
    print('first name is:' + user['firstname'])
    fname = user['firstname']