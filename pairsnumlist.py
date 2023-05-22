#program to print pairs in list and add to the given number
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
num=int(input("Enter the number:"))

print("Number pairs are:")
for i in range(0,n-1):
	for j in range(i+1,n):
		if a[i]+a[j]==num:
			print(a[i],"-",a[j])

		
	

		

			
		
		
		
		
				

