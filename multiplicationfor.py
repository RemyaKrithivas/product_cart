#program to print multiplication table up to n using for loop
n=int(input("Enter the number:"))
l=int(input("Enter the limit:"))
for i in range(1,l+1):
	print(i,"x", n,"=",i*n)