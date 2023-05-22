#program to insert list into another list
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
b=[]
m=int(input("Enter the number of elements in second list: "))
print("Enter the elements:")
for i in range(0,m):
	k=int(input())
	b.append(k)
	a.append(0)
index=int(input("enter the index:"))
for i in range(n-1,index-1,-1):
	a[i+m]=a[i]
for i in range(0,m):
	a[index+i]=b[i]
print("List elements are:")
for i in range(0,m+n):
	print(a[i])
			
		
		
		
		
				

