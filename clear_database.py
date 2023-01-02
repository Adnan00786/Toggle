import mysql.connector as database


with open('mysql_password.txt','r') as passwrd_read:
    PASSWORD_SQL = passwrd_read.read()

DATABASE = database.connect(host='localhost',user='root',passwd=PASSWORD_SQL)

if DATABASE.is_connected():
        print("System Connected to database..")
else:
        print("System cannot connect to database")

cursor_use = DATABASE.cursor()
cursor_use.execute("use togle")

query = 'truncate table customers'

print("Deleting customers..")
cursor_use.execute(query)


DATABASE.commit()

print("customers deleted")