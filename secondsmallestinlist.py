#program to print second smallest element in list
a=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(0,n):
	k=int(input())
	a.append(k)
small=a[0]
for i in range(1,n):
	if a[i]<small:
		small=a[i]
i=0
while(1):
	if a[i]!=small:
		ssmall=a[i]
		break
	i=i+1
for i in range(i+1,n):
	if a[i]>small and a[i]<ssmall:
		ssmall=a[i]
print("smallest is:",small)
print("second smallest is:",ssmall)