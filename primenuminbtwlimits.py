#program to print all prime numbers between two limits
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
if m<n and n!=1:
	print("prime numbers are:")
	for i in range(m,n+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			if i!=1:
				print(i)
else:
	print("Enter a valid input")

		
		
		
	