#program for prepare the ranklist of the student based on the subject mark
class student:
	def __init__(self,sname,srollno,subj1,subj2,subj3):
		self.stud_name=sname
		self.stud_rollno=srollno
		self.stud_mark1=subj1
		self.stud_mark2=subj2
		self.stud_mark3=subj3

	def stud_mark(self):
		self.stud_total=self.stud_mark1+self.stud_mark2+self.stud_mark3
	def display(self):
		print("Name				:",self.stud_name)
		print("Roll No				:",self.stud_rollno)
		print("Physics				:",self.stud_mark1)
		print("Chemistry				:",self.stud_mark2)
		print("Mathematics			:",self.stud_mark3)
		print("Total Marks			:",self.stud_total)
		print("----------------------------------------")

student_list=[]
n=int(input("Enter the number of students :"))
for i in range(0,n):
	nme=input("Enter the name of the student:")
	rno=int(input("Enter the roll number of the student:"))

	sub1=int(input("Enter the marks for Physics:"))
	sub2=int(input("Enter the marks for Chemistry:"))
	sub3=int(input("Enter the marks for Mathematics:"))
	stu=student(nme,rno,sub1,sub2,sub3)
	stu.stud_mark()
	student_list.append(stu)
for s in student_list:
	student_list[i].display()
for i in range(0,n-1):
	for j in range(i+1,n):
		if student_list[i].stud_total<student_list[j].stud_total:
			mark=student_list[i]
			student_list[i]=student_list[j]
			student_list[j]=mark
print("Rank\tName\tRollno\tTotal")
for i in range(0,n):
	print(i+1,"\t",student_list[i].stud_name,"\t",student_list[i].stud_rollno,"\t",student_list[i].stud_total)




