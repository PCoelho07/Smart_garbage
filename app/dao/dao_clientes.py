# -*- coding: utf-8 -*-

import csv
from models.cliente import * 
from models.lixeira import *
from dao_lixeiras import * 


class DaoClientes(object):

    def __init__(self, bairro = Bairro):
        self.__bairro = bairro

    def get_clientes_interessados(self):
        list_coleta = []
        
        file_path = 'app/files/'+ str(self.__bairro.get_nome()) + '.csv'

        data = csv.reader(open(file_path, 'r'))

        dao_lixeira = DaoLixeiras(self.__bairro)
        list_lixeira = dao_lixeira.get_lixeiras_from_csv()

        for rows in data:
            lixeira = Lixeira(rows[1])
            cliente = Cliente(rows[0], lixeira)
            list_coleta.append(cliente)

        return list_coleta