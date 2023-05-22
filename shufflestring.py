#program to shuffle the given string
word=input("enter a word:")
newstring=""
k=len(word)
i=0
j=k-1
while i<k//2:
	newstring+=word[i]
	newstring+=word[j]
	i+=1
	j-=1
if k%2!=0:
	newstring+=word[i]
print(newstring)
	