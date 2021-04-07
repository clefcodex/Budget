class Budget:

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance


	def deposit(self, amount):
		self.balance += amount
		print(f'deposit is successful. \n{self.name} current balance is ${self.balance}')

	def withdraw(self, amount):
		self.balance -= amount
		print(f'withdrawal is successful. \n{self.name} current balance is ${self.balance}')

	def get_balance(self):
		print(f'{self.name} current balance is ${self.balance}')

	def transfer(self, amount, category):
		category.balance += amount
		self.balance -= amount
		print(f'${amount} has been sent to {category.name} \n{self.name} current balance is ${self.balance}')


# instatiating food and clothing objects with initial deposit of $10000
food = Budget('Food', 10000)
clothing = Budget('Clothing', 10000)

food.get_balance()
clothing.get_balance()
print('')

# testing the deposit method
food.deposit(4000)
clothing.get_balance()
print('')

# testing the withdraw method
food.withdraw(2000)
clothing.get_balance()
print('')

#testing the tranfer method
food.transfer(2000, clothing)
clothing.get_balance()
print('')

