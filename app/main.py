# -*- coding: utf-8 -*-

from controllers import *
from models import *

def case_1():
    bairro_nome = raw_input('\n Digite o nome do bairro:')
    bairro = Bairro(bairro_nome)
    rota_controller = RotaController()
    rota_controller.calcular_rota(bairro)


mapeamentos = {1: case_1, 2: case_2}

def escolha(opcao):






print('\n\n---------------- Smart Garbage ---------------')
print('| Uma solução inteligente para coleta de lixo |')
print('| ___________________________________________ |')


opcao = 1
while opcao != 0:
    print('\n\n Escolha as opções abaixo:')
    print(' [0] Sair do programa ')
    print(' [1] Calcular rota ')
    print(' [2] Listar rotas ')

    opcao = input(" :>> ")
