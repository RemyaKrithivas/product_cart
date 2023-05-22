#program to print the list elements in ascending order using bubble sort
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

for i in range(0,n-1):
	min=a[i]
	pos=i
	for j in range(i+1,n):
		if a[j]<min:
			min=a[j]
			pos=j
	if i!=pos:
		temp=a[i]
		a[i]=a[pos]
		a[pos]=temp
print("Sorted elements are:")
for i in range(0,n):
	print(a[i])




			
		
		
		
		
				

