#program to print pattern
n=int(input("Enter the count:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i,end=" ")
	print()