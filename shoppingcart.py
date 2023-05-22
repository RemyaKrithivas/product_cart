class ShoppingCart:
	def __init__(self,qpa,qpb,qpc):
		self.quantity_of_productA=qpa
		self.quantity_of_productB=qpb
		self.quantity_of_productC=qpc	
		self.gift_wrap_fee=gwf
		self.shipping_fee=0

	def sub_total(self):
		self.total_of_productA=20*qpa
		self.total_of_productB=40*qpb
		self.total_of_productC=50*qpc
		self.sub_total=self.total_of_productA+self.total_of_productB+self.total_of_productC
		self.total_unit=qpa+qpb+qpc
	
	def discount_rule(self):
		if (self.sub_total>200):
			self.discount_price=self.sub_total-(self.sub_total*10/100)
			print("")
			
	

	def display(self):
		print("Product A				:",self.quantity_of_productA)
		print("Product B				:",self.quantity_of_productB)
		print("Product C				:",self.quantity_of_productC)
		print("Total of Product A		:",self.total_of_productA)
		print("Total of Product B		:",self.total_of_productB)
		print("Total of Product C		:",self.total_of_productC)
		print("Sub Total				:",self.sub_total)
		print("----------------------------------------")

cart_item=[]
qpa=input("Enter the quantity of product A:")
qpb=input("Enter the quantity of product B:")
qpc=input("Enter the quantity of product C:")
qwf=input("Product is wrapped as gift(yes/no)")
if qwf == "yes":
    print("You answered yes")
	return"yes"
else gwf == "no":
    print('You answered no.')
	return"no"

