#program for exception error handling using finally block
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
	c=a/b
except:
	c=a/(b+2)
	print("Division by zero not permitted")
else:
	print("No exception generated")
finally:
	print("Result is ",c)