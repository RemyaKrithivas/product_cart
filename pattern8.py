#program to print pattern
n=int(input("Enter the count:"))
for i in range(n,0,-1):
	for j in range(n,i-1,-1):
		print(i,end=" ")
	print()