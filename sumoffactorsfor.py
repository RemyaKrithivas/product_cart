#program to calculate the factors sum using forloop
n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
	if n%i==0:
		s=s+i
print("factors sum is:",s)
    

