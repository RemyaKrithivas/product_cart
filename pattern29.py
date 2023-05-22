#program to generate a pattern
n=int(input("Enter the number of lines:"))
for i in range(n,0,-1):
	for j in range(n,0,-1):
		if i<j:
			print(" ",end=" ")
		else:
			print(i,end=" ")
	print()