from bairro import *

class Rota(object):

	def __init__(self, bairro = None):
		if bairro is not None:	
			self.__bairro = bairro

		self.__list_lixeira = None 
		self.__list_coleta = None
		self.__melhor_rota = None
		self.__rota_regular = True


	def is_rota_regular(self):
		return self.__rota_regular

	def __gerar_lista_lixeiras(self):
		pass

	def __gerar_rota_padrao(self):
		pass

	def __gerar_rota_personalizada(self):
		pass




