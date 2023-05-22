#program to find the highest digit in a number using while
n=int(input("Enter the number:"))
s=9
while n!=0:
	d=n%10
	if d<s:
		s=d
	n=n//10
print("The smallest digit is",s)
