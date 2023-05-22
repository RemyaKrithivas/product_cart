a=()
n=int(input("Enter the number of elements:"))
for i in range(0,n):
	no=int(input())
	a=a+(no,)
 
for i in range(0,n//2):
	if a[i]!=a[n-i-1]:
		
		print("The tuple is symmetric")
	else:
		print("The tuple  symmetric")

		
	