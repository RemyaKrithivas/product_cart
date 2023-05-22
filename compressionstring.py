#program for perform the data compression 
n=input("Enter a string:")
s=len(n)
a=[]
for i in range(0,s):
	a.append(n[i])
b=[]
for i in a:
	if i not in b:
		b.append(i)
for x in b:
	cnt=0
	for y in a:
		if y==x:
			cnt+=1
	print(x,cnt,end=" ")
	









