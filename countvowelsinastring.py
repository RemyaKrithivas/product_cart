#program to count vowels in a given string
word=input("enter a word:")
s=0
for letter in word:
	if letter in "aeiouAEIOU":
		s=s+1
print("NUmber of vowels:",s)
	
