from pessoa import *

class Cliente(Pessoa):

	def __init__(self, nome, cpf, endereco, lixo):
		Pessoa.__init__(nome, cpf, endereco)
		self.__lixo = lixo

	def get_lixo(self):
		return self.__lixo

	def set_lixo(self, value):
		self.__lixo = value