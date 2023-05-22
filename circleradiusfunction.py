#program to find the radius and circumference of a circle
def area(r):
	return(3.14*r**2)
def circumference(r):
	return(3.14*2*r)
radius=int(input("Enter the radius:")) 
print("Area is",area(radius))
print("Circumfernce is",circumference(radius))