#program to find the highest digit in a number using while
n=int(input("Enter the number:"))
b=0
while n!=0:
	d=n%10
	if d>b:
		b=d
	n=n//10
print("The biggest digit is",b)
