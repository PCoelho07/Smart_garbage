

class Pessoa(object):

	def __init__(self, nome, coord_x = None, coord_y = None):
		self.__nome = nome
		self.__coord_x = coord_x
		self.__coord_y = coord_y

	def get_nome(self):
		return self.__nome

	def get_coordenada_x(self):
		return self.__coord_x

	def get_coordenada_y(self):
		return self.__coord_y

	def set_coordenada_x(self, value):
		self.__coord_x = value

	def set_coordenada_y(self, value):
		self.__coord_y = value
