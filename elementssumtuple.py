#program to read elements of tuple and find the sum
a=()
n=int(input("Enter the Number of elements:"))
print("Enter the numbers")
for i in range(0,n):
	no=int(input())
	a=a+(no,)
print(a)
s=0
for i in range(0,n):
	s+=a[i]
print("Sum is",s)
