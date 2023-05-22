#program to print the sum of even numbers in the list
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
s=0
for i in range(0,n):
	if a[i]%2==0:
		s=s+a[i]
print("sum is:",s)