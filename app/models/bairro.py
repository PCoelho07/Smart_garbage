# -*- coding: utf-8 -*- 
class Bairro(object):

	def __init__(self, nome = '', lixo = '',  populacao = ''):
		self.__nome = nome
		self.__quantidade_lixo = lixo
		self.__populacao = populacao

	def get_nome(self):
		return self.__nome

	def get_lixo(self):
		return self.__quantidade_lixo

	def set_nome(self, value):
		self.__nome = value

	def set_quntidade_lixo(self, value):
		self.__quantidade_lixo = value
