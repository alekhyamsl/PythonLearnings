import mysql.connector as conn
# inside pypi we can find almost every package
# we have to install mysql as well before importing it
# to install go to terminal and paste pip install mysql-connector-python
# if it is showing pip is not recongnised go to file -> settings -> go to project
# -> python interpreter -> then select conda env -> select python version

# establishing connectivity b/w python and MySQL
# host is where SQL is installed, in this case it is installed in local machine
# when the DB is on cloud in companies then the host URL, username and password
# will be given by Admin
mydb = conn.connect(host="localhost",user = "root",passwd = "Alekhya@99")
print(mydb) # checks if connection is established , if no errors are seen connection is established sucessfully
# cursor is the pointer which will be able to perform one one by operations
cur=mydb.cursor()
#cur.execute("create database Alekhya")
#cur.execute("show databases")
#print(cur.fetchall())
#cur.execute("create table alekhya.ineuron(emp_id int(10),emp_name varchar(100),emp_emailID varchar(20),emp_salary int(10),emp_attendence int(3))")

q2 = cur.execute("select * from alekhya.ineuron")
print(q2)

# based on query exceution planner we can optimize the queries

