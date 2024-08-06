import mysql.connector as conn
mydb = conn.connect(host="localhost",user = "root",passwd = "Alekhya@99")
print(mydb)
cursor = mydb.cursor()
cursor.execute("insert into alekhya.ineuron values(101,'alekhya','alekhya@gmail.com',100,30)")
# in Data bases commit is required to insert data into tables
mydb.commit()
cursor.execute("select * from alekhya.ineuron")
for i in cursor.fetchall():
    print(i)
