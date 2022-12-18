import mysql.connector as database

DATABASE = database.connect(host='localhost',user='root',passwd='9801!adnan')

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