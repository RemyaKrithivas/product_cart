
#program to check for the occurance of a given sublist in given list
a=[]
n=int(input("Enter the number of elements in the first list: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
b=[]
m=int(input("Enter the number of elements in the second list: "))
print("Enter the elements:")
for i in range(0,m):
	k=int(input())
	b.append(k)

for i in range(0,n-m+1):
	if a[i:i+m]==b:
		print("Yes in the list")
		break
else:
	print("Not in the List")
	
			

		
		
		
		
				
