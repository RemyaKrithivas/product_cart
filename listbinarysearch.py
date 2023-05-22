#program to search list elements  using binary search
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements in ascending order:")
for i in range(0,n):
	k=int(input())
	a.append(k)
key=int(input("Enter the element to search:"))
l=0
u=n-1
while l<=u:
	mid=(l+u)//2
	if a[mid]==key:
		print(key,"found at index",mid)
		break
	elif a[mid]>key:
		u=mid-1
	else:
		l=mid+1
else:
	print(key,"Not in the list")


			
		
		
		
		
				

