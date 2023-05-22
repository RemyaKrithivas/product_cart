#program to find the sum of n even numbers using while loop
n=int(input("Enter the limit:"))
i=2
s=0
while i<=n:
	s=s+i
	i=i+2
print("Sum is:",s)