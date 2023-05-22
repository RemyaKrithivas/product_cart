import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",
password="root123",
database="studentdetails"
)
mycursor=mydb.cursor()
sql= "INSERT INTO student(name,address)VALUES(%s,%s)"
val= [('ann','yyy,klm'),
	('midhun','zzz,ekm'),
	('salim','aaa,kzd'),
	('maya','bbb,alpy')


	
	
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")

