##PYthon ^
from foods import foodSource

def programMenu():
	menu = input('''
		1_зделать заказ
		0_выйти 
		''')
	return menu
def userСhoice():
	print(pullData[1]['food'])
	What = input('__выбирите еду по одной__ 0_выйти\n')
	return What
def checkPurchase():
	manyYou  = 1000
	m = manyYou - pullData[0][what]['many']
	pullData[0][what]['wholeMeal'] -= 1
	return m
def YouOrders():
	orders_sd.append([what])
	return orders_sd
def programLogic():
	if Menu == '1':
		print(pullData[1]["food"])
		if what in pullData[1]['food']:
			if pullData[0][what]['wholeMeal'] > 0:
				print('извините но этой еды больше нет')

				Purchase
				orders
		elif what not in pullData[1]['food']:
			print('извините у нас такого нет')
		
pullData     = foodSource()

orders_sd    = []
while True:
	print('_' * 79) 
	Menu     = programMenu()
	what     = userСhoice()
	Purchase = checkPurchase()
	orders   = YouOrders()
	print('осталось еды       :', pullData[0][what]['wholeMeal'], '\n'\
	      'ваша сума          :', Purchase,                       '\n'\
	      'вы зделали покупак :', orders,                         '\n')
	logic    = programLogic()
	if Menu == '0':
		break
