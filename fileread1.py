f=open("content.txt","r")
a=f.readline()
while a:
	print(a,end="->")
	a=f.readline()
f.close()