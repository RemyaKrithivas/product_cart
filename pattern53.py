#program to generate a pattern
n=int(input("Enter the number of lines:"))
for i in range(n,0,-1):
	for j in range(1,n+1):

		if i>j:
			print(" ",end=" ")
		else:
			print(i,end=" ")
	for k in range(n-1,i-1,-1):
		
			print(i,end=" ")
	print("")