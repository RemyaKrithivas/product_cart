#program to read list elements and  print the prime  elements
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0,n):
	k=int(input())
	a.append(k)

print("prime numbers are: ")
for i in range(0,n):
	if a[i]==1:
		continue
	for j in range(2,a[i]):
		if a[i]%j==0:
			break
	else:
		print(a[i])
		
		
		
	