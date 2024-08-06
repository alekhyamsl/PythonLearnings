import mysql.connector as conn
mydb = conn.connect(host="localhost",user = "root",passwd = "Alekhya@99")
print(mydb)
cursor = mydb.cursor()
cursor.execute("select emp_id,emp_emailID from alekhya.ineuron")
"""
for i in cursor.fetchall():
    print(i)
"""

l = []
for j in cursor.fetchall():
    l.append(j)

print(l)