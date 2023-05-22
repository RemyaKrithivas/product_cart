#program to generate string pattern
word=input("enter a word:")
k=len(word)
for i in range(1,k+1):
	print(word[0:i])
	