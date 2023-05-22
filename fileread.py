f=open("content.txt","r")
x=f.read()
vowel="aeiouAEIOU"
cnt=0
for letter in x:
	if letter in vowel:
		cnt=cnt+1
print(cnt)
f.close()