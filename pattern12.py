#program to print pattern
n=int(input("Enter the count:"))
for i in range(1,n+1):
	for j in range(n,i-1,-1):
		print("* ",end=" ")
	print()
for i in range (2,n+1):
	for j in range(1,i+1):
		print("* ",end=" ")
	print()