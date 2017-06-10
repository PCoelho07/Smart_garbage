from pessoa import *

class Cliente(Pessoa):

	def __init__(self, nome, cpf, endereco, lixeira):
		Pessoa.__init__(nome, cpf, endereco)
		self.__lixeira = lixeira

	def get_lixeira(self):
		return self.__lixeira

	def set_lixeira(self, value):
		self.__lixeira = value