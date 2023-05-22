#program for customized exception error handling using raise exception
a=input("Enter a your name: ")
age=int(input("Enter your age: "))
if age<18:
	raise Exception("You should be atleast 18 years old to entroll in voters list")
else:
	print(name,"is entrolled in voters list")
