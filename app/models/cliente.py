from pessoa import *

class Cliente(Pessoa):

	def __init__(self, nome, coord_x, coord_y, id, lixeira = None):
		Pessoa.__init__(nome, coord_x, coord_y)
		self.__lixeira = lixeira
		self.__id = id

	def get_lixeira(self):
		return self.__lixeira

	def set_lixeira(self, value):
		self.__lixeira = value