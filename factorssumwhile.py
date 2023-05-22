#program to calculate the factors sum using while
n=int(input("Enter the number:"))
i=1
s=0
while i<=n:
	if n%i==0:
		s=s+i
	i=i+1
print("factors sum is:",s)
    

