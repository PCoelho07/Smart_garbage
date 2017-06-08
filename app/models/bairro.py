
class Bairro(object):
	
	def __init__(self, nome='', lixo='', populacao=''):
		self.__nome = nome
		self.__lixo = lixo
		self.__populacao = populacao
		
	def get_nome(self):
		return self.__nome
		
	def get_lixo(self):
		return self.__lixo

	def set_nome(self, value):
		self.__nome = value

	def set_lixo(self, value):
		self.__lixo = value
