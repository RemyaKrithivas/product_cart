#program to find the binary equalent of a given decimal number 
d=int(input("Enter the decimal number:"))
b=0
i=0
while d!=0:
	r=d%2
	b=b+(r*(10**i))
	i=i+1
	d=d//2
print("Binary equalent is",b)
	
	
	 


