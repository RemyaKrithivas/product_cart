import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)
mycursor=mydb.cursor()
sql= "INSERT INTO student(name,address)VALUES(%s,%s)"
val= ('Kiran','xxx,tvm')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")

