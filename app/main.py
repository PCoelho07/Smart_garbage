# -*- coding: utf-8 -*-

import sys
from controllers.rota_controller import *
from models.bairro import *

lista_rotas = []

def trata_string(text):
    text_broken = text.lower().split()
    new_text = text_broken[0] + '_' + text_broken[1]
    return new_text
    

def case_1():
    bairro_nome = raw_input('\n Digite o nome do bairro: ')
    if bairro_nome == '':
        raise Exception("Bairro não deve ser vazio")
    
    bairro_nome = trata_string(bairro_nome)

    bairro = Bairro(bairro_nome)
    rota_controller = RotaController()
    rota_final = rota_controller.calcular_rota(bairro)
    lista_rotas.append(rota_final)
    print('\n\n Melhor Rota: {}'.format(rota_final))



def case_2():
    for rotas in lista_rotas:
        print(rotas)


def sair():
    print('\n\n Você saiu do programa!\n\n')
    sys.exit(0)

mapeamentos = {0: sair, 1: case_1, 2: case_2}

def escolha(opcao):
    mapeamentos[opcao]()




print('\n\n---------------- Smart Garbage ---------------')
print('| Uma solução inteligente para coleta de lixo |')
print('| ___________________________________________ |')


controle = True
opcao = ''
while controle:
    print('\n\n Escolha as opções abaixo:')
    print(' [0] Sair do programa ')
    print(' [1] Calcular rota ')
    print(' [2] Listar rotas ')

    opcao = input(" :>> ")

    escolha(opcao)