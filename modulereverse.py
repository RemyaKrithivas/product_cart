#program for module reverse 
def reverse(n):
	r=0
	while n!=0:
		d=n%10
		r=(r*10)+d
		n=n//10
	print("reverse is",r)
def digitsum(n):
	r=0
	while n!=0:
		d=n%10
		r=r+d
		n=n//10
	print("sum is is",r)
