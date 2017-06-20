# -*- coding: utf-8 -*-
from cliente import *
import random

def calcula_proximo(clientlist, x_atual, y_atual, primeiro):
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


if __name__ == '__main__':

	clientlist = []
	lista_atual = []
	for count in range(4):
		c_x = random.randint(-10, 11)
		c_y = random.randint(-10, 11)
		x = Cliente("", c_x, c_y, count, None)
		clientlist.append(x)

	while clientlist.length > 0:
		atual = calcula_proximo(clientlist, 0, 0, 0)
		lista_atual.append(atual)
		for c in clientlist:
			if c.id == atual:
				clientlist.remove(c)

	print("Rota planejada")
