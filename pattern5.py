#program to print pattern
n=int(input("Enter the count:"))
for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()