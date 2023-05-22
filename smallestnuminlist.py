#program to read list elements and  print the smallest element in the list
a=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
small=a[0]
for i in range(1,n):
	if a[i]<small:
		small=a[i]
		
print("Smallest number is:",small)