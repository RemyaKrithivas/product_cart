#program to check whether a number prime or composite using for loop
n=int(input("Enter the number:"))
if n!=1:
	for i in range(2,n):
		if n%i==0:
			print("Number is composite")
			break
	else:
		print("Number is prime")

elif n==1 or n==0:
	print("Number is neither prime or composite")
else:

	print("Number is prime")
