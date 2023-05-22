#program for default argument using to claculate simple interest
def simple_interest(p,t,r=5):
	i=p*r*t/100
	return i
		
principle_amount=int(input("Enter the principle amount: "))
time_period=int(input("Enter the time period: "))
rate_of_interest=int(input("Enter the rate of interest: "))
i1=simple_interest(principle_amount,time_period)
print("Interest: ",i1)
i2=simple_interest(principle_amount,time_period,rate_of_interest)
print("Interest: ",i2)


		

		
