#program to print grade of a student

m1=int(input("Enter the  fist subject mark: "))
m2=int(input("Enter the  second subject mark: "))
m3=int(input("Enter the  third subject mark: "))
t=m1+m2+m3
p=t/100*300
if(p>=90):
	print("grade A+")
elif(p<90 and p>=80):
	print("grade A")
elif(p<80 and p>=70):
	print("grade B+")
elif(p<70 and p>=60):
	print("grade B")
elif(p<60 and p>=50):
	print("grade C")
else:
	print("Failed")



