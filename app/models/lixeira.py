# -*- coding: utf-8 -*-
class Lixeira(object):

	def __init__(self,  identificador, coord_x, coord_y, quantidade ='', tipo_lixo = ''):
		self.__identificador = identificador
		self.__coord_x = coord_x
		self.__coord_y = coord_y
		self.__quantidade = quantidade
		self.__tipo_lixo = tipo_lixo
	
	def get_identificador(self):
		return self.__identificador

	def get_quantidade(self):
		return self.__quantidade

	def get_tipo_lixo(self):
		return self.__tipo_lixo

	def set_tipo_lixo(self, value):
		self.__tipo_lixo = value

	def set_quantidade(self, value):
		self.__quantidade = value

	def get_coordenada_x(self):
		return self.__coord_x

	def get_coordenada_y(self):
		return self.__coord_y

	def set_coordenada_x(self, value):
		self.__coord_x = value

	def set_coordenada_y(self, value):
		self.__coord_y = value
