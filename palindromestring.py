#program to check whether a given string is palindrome or not
word=input("enter a word:")
k=len(word)
for i in range(0,k//2):
	if word[i]!=word[k-i-1]:
		print("Not a Palindrome")
		break
else:
	print(" Palindrome")

	
