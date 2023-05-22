#program to insert an element into a list at given index
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
a.append(0)
element=int(input("Enter which element add to the list:"))
index=int(input("Enter the index:"))
for i in range(n,index,-1):
	a[i-1]=a[i]
	a[index]=element
print("List elements are:")
for i in range(0,n+1):
	print(a[i])

			
		
		
		
		
				

