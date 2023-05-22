#program to check whether the roots of a quandratic equation real or imaginary

a=int(input("enter the coefficient of x^ term: "))
b=int(input("enter the coefficient of x term: "))
c=int(input("enter the coefficient of constant: "))
s=(b**2-(4*a*c))

if s>0:
	x1=(-b+s**0.5)/2*a
	x2=(-b-s**0.5)/2*a
	print("the roots are",x1,x2)
elif s==0:
	x1=-b/(2*a)
	print("the roots is",x1)
else:
	print("the roots are imaginary")


 
