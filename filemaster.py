f=open("master.txt","w")
n=int(input("Enter the count:"))
for x in range(n):
	num=input("Enter a number:")
	num=num+"\n"
	f.write(num)
f.close()
p=open("even.txt","w")
q=open("odd.txt","w")
f=open("master.txt","r")
for i in range(0,n):
	a=int(f.readline())
	if a%2==0:
		p.write(str(a)+"\n")
	else:
		q.write(str(a)+"\n")
p.close()
q.close()
f.close()