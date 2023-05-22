#program to print factors of a numbers using while
n=int(input("Enter the number:"))
i=1
print("factors are:")

while i<=n:
	if n%i==0:
		print(i)
	i=i+1

