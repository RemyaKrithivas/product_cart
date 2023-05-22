#program to print the list elements in ascending order using bubble sort
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

for i in range(0,n-1):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print("Sorted elements are:")
for i in range(0,n):
	print(a[i])




			
		
		
		
		
				

