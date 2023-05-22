#program to sum of even numbers up to n using for loop
n=int(input("Enter the limit:"))
s=0
for x in range(2,n+1,2):
	s=s+x
print("Sum is:",s)