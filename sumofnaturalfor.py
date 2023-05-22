#program to sum of n natural numbers using for loop
n=int(input("Enter the limit:"))
s=0
for x in range(1,n+1,1):
	s=s+x
print("The sum is:",s)