#program to generate a pattern 
n=int(input("Enter the number of lines:"))
for x in range(n,0,-1):
	for i in range(1,x+1):
		for j in range(n,0,-1):
			if i<j:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		for k in range(2,i+1):
			print("*",end=" ")
		print("")
