#program to find biggest among three number

a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
if a>b and a>c:
	big=a
elif b>a and b>c:
	big=b
else:
	big=c
print("biggest is:", big)
