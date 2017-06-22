# -*- coding: utf-8 -*-

from controllers.rota_controller import *
from models.bairro import *

lista_rotas = []

def case_1():
    bairro_nome = raw_input('\n Digite o nome do bairro:')
    
    if bairro_nome == ' ':
        raise Exception("Bairro não deve ser vazio")

    bairro = Bairro(bairro_nome)
    rota_controller = RotaController()
    rota_final = rota_controller.calcular_rota(bairro)
    lista_rotas.append(rota_final)
    print("Melhor Rota:", rota_final)

def case_2():
    for rotas in lista_rotas:
        print(rotas)


def case_default():
    print('Digite uma opção válida  ')

mapeamentos = {1: case_1(), 2: case_2}

def escolha(opcao):
    try:    
        mapeamentos[opcao]
    except:
        case_defaut()




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

    escolha(opcao)