#program to print fibonacci series using while loop
n=int(input("Enter the limit:"))
f1=0
f2=1
if n==1:
	print(f1)
elif n==2:
	print(f1,f2)
elif n<=0:
	print("No Series")
else:
	print(f1,end=" ")
	print(f2,end =" ")
	i=2
	while n>i:
		f3=f1+f2
		print(f3,end=" ")
		f1=f2
		f2=f3
		i=i+1
		