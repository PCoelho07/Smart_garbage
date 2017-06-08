
class Lixo(object):
	
	def __init__(self, quantidade ='', tipo_lixo = ''):
		self.__quantidade = quantidade
		self.__tipo_lixo = tipo_lixo

	def get_quantidade(self):
		return self.__quantidade

	def get_tipo_lixo(self):
		return self.__tipo_lixo
	
	def set_tipo_lixo(self, value):
		self.__tipo_lixo = value

	def set_quantidade(self, value):
		self.__quantidade = value
		