from pessoa import *

class Cliente(Pessoa):

	def __init__(self, nome, identificador, lixeira = None):
		Pessoa.__init__(nome, lixeira.get_coordenada_x(), lixeira.get_coordenada_y())
		self.__lixeira = lixeira
		self.__identificador = identificador

	def get_lixeira(self):
		return self.__lixeira

	def set_lixeira(self, value):
		self.__lixeira = value

	def get_identificador(self):
		return self.__identificador

	def set_identificador(self, value):
		self.__identificador = value
