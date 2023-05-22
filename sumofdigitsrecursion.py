#program for sum of digits in a number using recursive function
def sum_digits(n):
	if n==0:
		return 0
	s=n%10+sum_digit(n//10)
num=int(input("Enter the number:"))
sum=sum_digits(num)
print("Sum is:",sum)