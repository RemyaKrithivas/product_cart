#program to delete the list element at given index
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
	
index=int(input("enter the index:"))
for i in range(index,n-1):
	a[i]=a[i+1]
n=n-1
print("List elements are:")
for i in range(0,n):
	print(a[i])
			
		
		
		
		
				

