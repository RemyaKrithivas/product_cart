# program to find the basic salary of an employee usin elif

bs=int(input("enter the basic salary of an employee: "))

if (bs<=5000):

	da=(25/100)*bs
	hra=(30/100)*bs
	pf=(3/100)*bs

elif bs>=5000 and bs<10000:
	
	da=(20/100)*bs
	hra=(27/100)*bs
	pf=(3.5/100)*bs

elif bs>=10000 and bs<15000:

	da=(18/100)*bs
	hra=(22/100)*bs
	pf=(4/100)*bs

else:

	da=(15/100)*bs
	hra=(20/100)*bs
	pf=(5/100)*bs

      
ns=bs+da+hra-pf

print("Net salary of an employee:",ns)

