#program to delete duplicate elements from the list
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
i=0
while i<n-1:
	j=i+1
	while j<n:
		if a[i]==a[j]:
			a.pop(j)
			n=n-1
		else:
			j+=1
	i+=1

print("List elements are:")
print(a)
		
