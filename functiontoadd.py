#program for function add two or more numbers
def my_function(*numbers):
	s=0
	for x in numbers:
		s=s+x
	print("sum is:",s)
my_function(10,20)
my_function(10,20,30,40,50)
my_function(10.2,2.5)
		

		
