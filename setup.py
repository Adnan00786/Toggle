import mysql.connector as database

PASSWORD_SQL = input("Enter Mysql Password: ")

DATABASE = database.connect(host='localhost',user='root',passwd=PASSWORD_SQL)

if DATABASE.is_connected():
        print("System Connected to database..")
else:
        print("System cannot connect to database")

with open('mysql_password.txt','a') as passwrd_writer:
    passwrd_writer.write(PASSWORD_SQL)

def EXECUTE():
    cursor_use = DATABASE.cursor()
    cursor_use.execute("Create Database toggle")

    cursor_use.execute("Use togle")


    cursor_use.execute('''
    create Table customers(    
                            cust_name VARCHAR(30),
                            cust_id  INT PRIMARY KEY AUTO_INCREMENT,
                            cust_pass CHAR(8),
                            cust_gender CHAR(1),
                            cust_birth_date INT,
                            cust_Weight DECIMAL,
                            cust_email varchar(320),
                            cust_height DECIMAL,
                            cust_age INT
                            ); 
                        ''')


try:
    EXECUTE()
except Exception as error:
    print("Error: ",error)    