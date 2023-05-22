#program to read list elements and  print that elements
a=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
big=a[0]
for i in range(1,n):
	if a[i]>big:
		big=a[i]
		
print("bigest number is:",big)