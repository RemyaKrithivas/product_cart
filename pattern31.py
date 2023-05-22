#program to generate a pattern
n=int(input("Enter the number of lines:"))
for i in range(n,0,-1):
	for j in range(1,n+1):
		if i>j:
			print(" ",end=" ")
		else:
			print(i,end=" ")
	print()

for i in range(2,n+1):
	for j in range(1,n+1):
		if i>j:
			print(" ",end=" ")
		else:
			print(i,end=" ")
	print()