#program to merge list elements without using sort
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
b=[]
m=int(input("Enter the number of elements in second list: "))
print("Enter the elements:")
for i in range(0,m):
	k=int(input())
	b.append(k)
c=[]
i=0
j=0
while i<n and j<m:
	if a[i]<b[j]:
		c.append(a[i])
		i=i+1
	else:
		c.append(b[j])
while i<n:
	c.append(a[i])
	i+=1
while j<m:
	c.append(b[j])
	j+=1

print("Merged list:")
for i in range(0,m+n):
	print(c[i])
			
		
		
		
		
				

