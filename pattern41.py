#program to generate a pattern
n=int(input("Enter the number of lines:"))
k=1
for i in range(1,n+1):
	for j in range(1,i+1):
			print(k,end=" ")
			k+=1
	print()