import utils


class Monster:
	def __init__(self):
		self.reset()

	def reset(self, class_):
		# inits
		config= utils.load_yaml(utils.MOB_CONFIG)[class_]

		# set numerical stats
		for x,y in config.items():
			self.__setattr__(x,y)

		# convert certain stats to [current, max, ratio] list
		for x in ["hp"]:
			tmp= [self.__getattribute__(x), self.__getattribute__(x), 1.0]
			self.__setattr__(x, tmp)