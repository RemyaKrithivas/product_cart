#program to generate a pattern 
n=int(input("Enter the number of lines:"))
for x in range(1,n+1):
	for i in range(0,n):
		for j in range(n,0,-1):
			if j>x:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		for k in range(2,x+1):
			print("*",end=" ")
		print("")
