#program to check whether a number is perfect or not using while
n=int(input("Enter the number:"))
i=1
s=0
while i<n:
	if n%i==0:
		s=s+i
	i=i+1
if s==n:
	print("Perfect")
else:
	print("Not Perfect")
