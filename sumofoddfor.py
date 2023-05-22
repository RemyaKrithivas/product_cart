#program to sum of odd  numbers up to n using for loop
n=int(input("Enter the limit:"))
s=0
for a in range(1,n+1,2):
	s=s+a
print("Sum is:",s)
	