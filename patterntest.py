#program to generate a pattern
n=int(input("Enter the number of lines:"))
for i in range(1,n+1):
	for j in range(1,i+1):
		if j<=n:
			print(i,end=" ")
			i=i+1
			j=j+1
	print()