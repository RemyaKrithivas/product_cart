#program to search an element from the given list 
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)

element=int(input("Enter which element to search in the list:"))
for i in range(0,n):
     
	if a[i]==element:
		print(element," in the list ")
		break
else:
	print(element," not in the list ")


			
		
		
		
		
				

