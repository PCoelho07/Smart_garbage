from pessoa import *

class Cliente(Pessoa):

	def __init__(self, nome, cpf = '', coord_x, coord_y, lixeira = None):
		Pessoa.__init__(nome, cpf, coord_x, coord_y)
		self.__lixeira = lixeira

	def get_lixeira(self):
		return self.__lixeira

	def set_lixeira(self, value):
		self.__lixeira = value