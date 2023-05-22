#check whether a number prime or composit using while
n=int(input("Enter the number:"))
if n!=0 and n!=1:
	i=2
	while i<=n:
		if n%i==0:
			print("The number is composite")
			break
		i=i+1
	else:
		print("The number is prime")
else:	
	print("The number is neither prime nor composite")
	
	