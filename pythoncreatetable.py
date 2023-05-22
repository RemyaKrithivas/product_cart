import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)
mycursor=mydb.cursor()
mycursor.execute("create table student(name varchar(255),address varchar(255))")

