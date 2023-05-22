#program to find the factorial of a numbers using for loop
n=int(input("Enter the number:"))
f=1
for x in range(2,n+1):
	f=f*x
	
print("factorial is",f)
