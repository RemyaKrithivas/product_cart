#program to print fibinocci series using for loop
n=int(input("Enter the limit:"))
f1=0
f2=1
if n<=0:
	print("No Series")
elif n==1:
	print(f1)
elif n==2:
	print(f1)
	print(f2)
else:
	print(f1)
	print(f2)
	n=n-2
	for i in range(n,0,-1):
		f3=f1+f2
		print(f3)
		f1=f2
		f2=f3
	
	
		

