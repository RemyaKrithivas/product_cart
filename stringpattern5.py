#program to generate a pattern
word=input("enter a word:")
k=len(word)
for i in range(1,k+1):
    for j in range(k ,0,- 1):
		if j==1:
        		print('word[j-1] ', end='')
		else:
			print(" ",end=" ")
    for k in range(1,i):
        if k==i-1:
            print(word[k], end='')
		 m+=1
        else:
            print(' ', end='')
    print()
m=k-2
for i in range(2,k+1):
    for j in range(i,k+1):
		if j==1:
			print(word[m], end='')
		else:
			print(' ', end='')
    for n in range(k,i,-1):
        if n ==i+1:
            print(word[n], end='')
		m-=1
        else:
            print(' ', end='')
    print()
