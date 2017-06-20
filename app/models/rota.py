# -*- coding: utf-8 -*-

from bairro import *
from cliente import *
from dao_lixeiras import DaoLixeiras
import random

class Rota(object):

	def __init__(self, bairro):
		self.__bairro = bairro
		self.__list_lixeira = []
		self.__melhor_rota = ()

	def get_lixeiras(self):
		return self.__list_lixeira

	def get_bairro(self):
		return self.__bairro

	def set_bairro(self, value):
		self.__bairro = value

	def is_rota_regular(self):
		return self.__rota_regular

	def gerar_lista_lixeiras(self):
		data_lixeiras = DaoLixeiras(self.__bairro)
		self.__list_lixeira = data_lixeiras.get_lixeiras()

	def gerar_rota_personalizada(self, lista_coleta):
		if len(lista_coleta) <= 0:
			 return None

		lista_coleta_lixeiras = []
		for clientes in lista_coleta:
			lixeira_cliente = clientes.get_lixeira()
			id_cliente = clientes.get_id()
			t_cliente = (id_cliente, lixeira_cliente)

			lista_coleta_lixeiras.append(t_cliente)

	# ------------------- TO DO -------------------



	def gerar_rota_padrao(self, interested_list):
		while interested_list.length > 0:
			atual = self.__calcula_proximo(interested_list, 0, 0, 0)
			lista_atual.append(atual)
			for c in interested_list:
				if c.id == atual:
					interested_list.remove(c)

		return lista_atual

	def __calcula_proximo(self, clientlist, x_atual, y_atual, primeiro):
		mais_proximo_distancia = 100
		for c in clientlist:
			distancia = math.sqrt( ((0 - c.coord_x)**2) + ((0 - c.coord_y)**2))

			if primeiro == 0:
				primeiro = 1
				mais_proximo = c.id
				mais_proximo_distancia = distancia
				continue

			if distancia < mais_proximo_distancia:
				mais_proximo_distancia = distancia
				mais_proximo = c.id

		return mais_proximo
