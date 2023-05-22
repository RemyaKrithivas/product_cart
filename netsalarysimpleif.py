# program to find the basic salary of an employee usin simple if

bs=int(input("enter the basic salary of an employee: "))
da=(10/100)*bs
hra=(15/100)*bs
pf=(3/100)*bs

if (bs<=10000):
	da=(20/100)*bs
	hra=(25/100)*bs
	pf=(5/100)*bs
      
ns=bs+da+hra-pf

print("Net salary of an employee:",ns)

