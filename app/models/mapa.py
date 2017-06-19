from cliente import coord_x, coord_y, nome
import random

if __name__ == '__main__':

	clientlist = []
	for count in range(4):
		c_x = random.randint(-10, 11)
		c_y = random.randint(-10, 11)
		x = Cliente("", c_x, c_y, count, None)
		clientlist.append(x)

	def calcula_proximo():
		primeiro = 0
		mais_proximo = 0
		x_atual1 = x_atual
		y_atual1 = y_atual
		for c in clientlist:
			distancia = math.sqrt( ((0 - c.coord_x)**2) + ((0 - c.coord_y)**2))
			if primeiro == 0:
				primeiro = 1
				mais_proximo = c.id
		return mais_proximo



