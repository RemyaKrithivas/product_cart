#program to generate string pattern
word=input("enter a word:")
k=len(word)

for i in range(0,k):
	print(word[0:i])
	for j in range(i-1,0):
		print(" ",end="")

    