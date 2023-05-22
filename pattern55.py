#generate a pattern

n=int(input("Enter the maximum count:"))
for x in range(n,0,-1):
	for i in range(1,x+1):
		for j in range(n,0,-1):
			if j>i:
				print(" ",end=" ")
			else:
				print(j,end=" ")
		print(" ")
	for i in range(x-1,1,-1):
		for j in range(n,0,-1):
			if j>i:
				print(" ",end=" ")
			else:
				print(j,end=" ")
		print(" ")

for i in range(n,0,-1):
	if i>x:
		print(" ",end=" ")
	else:
		print(x,end=" ")
print(" ")