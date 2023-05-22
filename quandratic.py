#program to check whether the roots of a quandratic equation real or imaginary using if else

a=int(input("enter the coefficient of x^ term: "))
b=int(input("enter the coefficient of x term: "))
c=int(input("enter the coefficient of constant: "))
s=b**2-(4*a*c)

if (s>=0):
	print("root are real")
else:
	print("root are imaginary")

 
