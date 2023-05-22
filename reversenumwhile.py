#program to reverse of a given number using while
n=int(input("enter the number:"))
rev=0
while n!=0:
	d=n%10
	rev=(rev*10)+d
	n=n//10
print("Reverse is",rev)