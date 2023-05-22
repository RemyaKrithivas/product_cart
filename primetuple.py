a=()
n=int(input("Enter the number of elements:"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
 
print("prime numbers are: ")
for i in range(0,n):
	if a[i]==1:
		continue
	for j in range(2,a[i]):
		if a[i]%j==0:
			break
	else:
		print(a[i])
		
		
		
	