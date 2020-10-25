import utils

class Player:
	def __init__(self):

		# load numerical stats
		config= utils.load_yaml(utils.BATTLE_CONFIG)
		for x,y in config['player']['init'].items():
			self.__setattr__(x, y)