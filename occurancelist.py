#program to count occurance of the list
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
b=[]
for i in a:
	if i not in b:
		b.append(i)
for x in b:
	count=0
	for y in a:
		if y==x:
			count+=1
		
	print(x,"occured",count,"times")	
		
				

