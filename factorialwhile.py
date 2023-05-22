#program to find the factorial of a number using while loop
n=int(input("Enter the number :"))
f=1
i=1
while i<=n:
	f=f*n
	n=n-1
print("Factorial is:",f)
	