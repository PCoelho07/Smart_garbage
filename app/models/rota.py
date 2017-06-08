

class Rota(object):

	def __init__(self, enderecos = '', melhor_rota = ''):
		self.__enderecos = enderecos
		self.__melhor_rota = melhor_rota
		self.__rota_regular = True


	def get_enderecos(self):
		return self.__enderecos

	def is_rota_regular(self):
		return self.__rota_regular

	def get_melhor_rota(self):
		return self.__melhor_rota


	'''
		TO DO ANOTHER METHODS
	'''