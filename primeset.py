#program to print prime numbers in set
a=set()
n=int(input("Enter the number of elements:"))
print("Enter the numbers:")
for i in range(0,n):
	e=int(input())
	a.add(e)
 
print("prime numbers are: ")
for x in a:
	if x==1:
		continue
	for j in range(2,x):
		if x%j==0:
			break
	else:
		print(x)
		
		
		
	