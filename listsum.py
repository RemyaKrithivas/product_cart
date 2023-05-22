#program to read list elements and  print that elements
a=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
s=0
for i in range(0,n):
	s=s+a[i]
print("sum is:",s)