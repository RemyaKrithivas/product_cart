#program to find the sum of digits until the sum become a single digit
n=int(input("Enter the number:"))
s=0
while n!=0:
	d=n%10
	s=s+d
	n=n//10
	if n==0 and s>9:
		n=s
		s=0
print("sum is",s)
	
		
	
	 