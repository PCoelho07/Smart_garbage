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
			 raise Exception('Atributo deve ser uma lista não-vazia')

		lista_coleta.sort(key=lambda x: x.get_lixeira().get_quantidade(), reverse=True)
		rota_padrao = self.__vizinho_mais_proximo(self.__list_lixeira)
		rota_personalizada = list(lista_coleta + rota_padrao)

		return rota_personalizada


	def gerar_rota_padrao(self):
		pass

	def __vizinho_mais_proximo(self, interested_list):
		lista_atual = []
		lista_atual.append(interested_list[0].get_identificador())
		for item in interested_list:
			atual = self.__calcula_proximo(interested_list, item.get_coordenada_x(), item.get_coordenada_y(), 0)
			lista_atual.append(atual)
			for c in interested_list:
				if c.get_identificador() == atual:
					interested_list.remove(c)

		return lista_atual

	def __calcula_proximo(self, clientlist, x_atual, y_atual, primeiro):
		mais_proximo_distancia = 100
		for c in clientlist:
			distancia = math.sqrt( ((x_atual - c.coord_x)**2) + ((y_atual - c.coord_y)**2))

			if primeiro == 0:
				primeiro = 1
				mais_proximo = c.get_identificador()
				mais_proximo_distancia = distancia
				continue

			if distancia < mais_proximo_distancia:
				mais_proximo_distancia = distancia
				mais_proximo = c.get_identificador()

		return mais_proximo
