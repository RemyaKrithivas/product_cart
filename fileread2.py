f=open("content.txt","r")
a=f.readline()
vowel="aeiouAEIOU"
while a:
	cnt=0
	for x in a:
		if x in vowel:
			cnt+=1
	print(f'{cnt}vowels in {a}')
	a=f.readline()
f.close()