#program to swapping two numbers without using temporary variable

a=int(input("enter the first number "))
b=int(input("enter the second number "))
print("value of a before swapping",a)
print("value of b before swapping",b)
a=a+b
b=a-b
a=a-b
print("value of a after swapping",a)
print("value of b after swapping",b)

