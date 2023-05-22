#program to find biggest among three number using nested if

a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
if a>b:
	if a>c:
		big=a
	else:
		big=c
else:
	if b>c:
		big=b
	else:
		big=c
print("biggest is:",big)
	
