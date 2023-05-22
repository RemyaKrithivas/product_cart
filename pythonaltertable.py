import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)
mycursor=mydb.cursor()
mycursor.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

