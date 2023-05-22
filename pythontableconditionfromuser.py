import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)

mycursor=mydb.cursor()
addr=()
sql="SELECT * FROM student WHERE address= %s"
key=input("Enter an address:")
addr=addr+(key,)
mycursor.execute(sql,addr)
myresult=mycursor.fetchall()
for x in myresult:
	print(x)
	
