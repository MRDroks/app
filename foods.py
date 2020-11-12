def foodSource():
	#еды 
	food     = [
				 'pizza',
				'МОХИТО',
				'МЯТНОЕ',
				'МОЛОКО',
				  'АБОН'
		]
	#стоимость еды 
	foodСost = {
				'pizza':  {
				 			'many'     :100,
				 			'wholeMeal': 2
				},
				'МОХИТО':  {
							'many'     : 39,
							'wholeMeal': 28
			   	},
				'МЯТНОЕ':  {
							'many'     : 45,
							'wholeMeal':120
				},
				'МОЛОКО':  {
							'many'     : 28,
							'wholeMeal': 59
				},
				'АБОН':     {
							'many'     : 67,
							'wholeMeal': 55
				}
		}

	return [foodСost, {'food':food}]