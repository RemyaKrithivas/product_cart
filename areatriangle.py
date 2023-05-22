# program to find the area and perimeter of a scalane triangle

a=int(input("enter the first side of a triangle "))
b=int(input("enter the second side of a traigle: "))
c=int(input("enter the third side of a traingle:"))
p=a+b+c
s=p/2
ar=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of the traigle:",ar)
print("perimeter of the traigle:",p)
