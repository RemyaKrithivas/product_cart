#program to calculate electricity bill based on the condition

unit=int(input("enter the unit consumed:"))

if (unit<=100):
	charge=2*unit
else:
	charge=100*2+(unit-100)*3

print("electricity bill is:",charge)