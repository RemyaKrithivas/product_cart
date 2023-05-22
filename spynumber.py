#program to check whether a number is spy or not using while
n=int(input("Enter the number:"))
s=0
p=1
while n!=0:
	d=n%10
	s=s+d
	p=p*d
	n=n//10
if(s==p):
	print("Spy Number")
else:
	print("Not a spy number")
	