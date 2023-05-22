#program to check whether a given number is palindrome or not
n=int(input("enter the number:"))
num=n
rev=0
while n!=0:
	d=n%10
	rev=(rev*10)+d
	n=n//10
if rev==num:
	print("Number is Palindrome")
else:
	print("Number is not Palindrome")
