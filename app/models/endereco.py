
class Enderenco(object):

	def __init__(self, bairro='', rua='', numero='', referencia=''):
		self.__bairro = bairro
		self.__rua = rua
		self.__numero = numero
		self.__referencia = referencia

	def get_bairro(self): 
		return self.__bairro

	def get_rua(self): 
		return self.__rua

	def get_numero(self): 
		return self.__numero

	def get_referencia(self): 
		return self.__referencia