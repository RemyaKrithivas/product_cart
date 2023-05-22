#program for sum of natural number using recursive function
def naturalnum_sum(n):
	if n==1:
		return 1
	s=0
	s=n+naturalnum_sum(n-1)
	return s
no=int(input("Enter the number:"))
	s=naturalnum_sum(no)
print("Sum is:",s)