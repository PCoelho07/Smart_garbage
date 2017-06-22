# -*- coding: utf-8 -*-

import csv
from models.cliente import *
from models.lixeira import *
from dao_lixeiras import *


class DaoClientes(object):

    def __init__(self, bairro = None):
        self.__bairro = bairro
        self.__file_name = 'clientes'

    def get_clientes_interessados(self):
        list_coleta = []

        file_path = 'app/files/'+ str(self.__file_name) + '.csv'

        data = csv.reader(open(file_path, 'r'))

        dao_lixeira = DaoLixeiras(self.__bairro)
        list_lixeira = dao_lixeira.get_lixeiras_from_csv()

        for rows in data:
            for lx in list_lixeira:
                if rows[1] == lx.get_identificador():
                    cliente = Cliente(rows[0], lx)
                    list_coleta.append(cliente)

        return list_coleta
