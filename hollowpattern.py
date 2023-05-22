#program to generate a pattern
n=int(input("Enter the number of lines:"))
for i in range(1,n+1):
	for j in range(n,0,-1):
		if j==i:
			print(j ,end=" ")
		else:
			print(" ",end=" ")
	for k in range(2,i+1):
		if k==i:
			print(k,end=" ")
		else:
			print(" ",end=" ")
		
	print()
for i in range(n-1,0,-1):
	for j in range(n,0,-1):
		if i==j:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	for k in range(2,i+1):
		if i==k:
			print(k,end=" ")
		else:
			print(" ",end=" ")
	print()

		