from bairro import *

class Rota(object):

	def __init__(self, bairro = None):
		self.__bairro = bairro
		self.__list_lixeira = []
		self.__list_coleta = []
		self.__melhor_rota = []
		self.__rota_regular = True

	def get_bairro(self):
		self.__bairro

	def set_bairro(self, value):
		self.__bairro = value

	def is_rota_regular(self):
		return self.__rota_regular

	def __gerar_lista_lixeiras(self):
		pass
		# Pegar lixeiras do bairro correspondente ao bairro que se quer gerar a rota

	def __gerar_rota_padrao(self):
		pass
		# Gerar rota com base apenas na qunatidade de lixo por lixeira ou cliente que realizou solicitação

	def __gerar_rota_personalizada(self):
		pass
