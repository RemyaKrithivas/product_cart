#program for function arbitory argument
def my_function(*students):
	print(type(students))
	for x in students:
		print(x)
my_function("Kiran","Manu","Vinu")
my_function(10,20,30,40,50)