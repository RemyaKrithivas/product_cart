#program to n delete elements from the given index
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

num=int(input("Enter the number of elements deleted from the list:"))
index=int(input("Enter the index:"))
for i in range(index+num,n):
	a[i-num]=a[i]
n=n-num
	
print("List elements are:")
for i in range(0,n):
	print(a[i])

			
		
		
		
		
				

