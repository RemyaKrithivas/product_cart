import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM student")
myresult=mycursor.fetchall()
for x in myresult:
	print(x)
