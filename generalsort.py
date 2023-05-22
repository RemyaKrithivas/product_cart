#program to print the list elements in ascending order
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

for i in range(0,n-1):
	for j in range(i+1,n):
		if a[i]>a[j]:
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
print("Ascending order of a list:",a)




			
		
		
		
		
				

