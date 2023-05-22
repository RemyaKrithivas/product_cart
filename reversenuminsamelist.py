#program to reverse element in same list
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

for i in range(0,n//2):
	t=a[i]
	a[i]=a[n-i-1]
	a[i-n-1]=t
print("List elements are:")
for i in range(0,n):
	print(a)

		

			
		
		
		
		
				

