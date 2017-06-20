# -*- coding: utf-8 -*-
import csv
from models.lixeira import *
from models.bairro import *

class DaoLixeiras(object):

    """docstring for DaoLixeiras."""
    def __init__(self, bairro = Bairro):
        self.__bairro_nome = bairro.get_nome()


    def get_lixeiras(self):
        list_lixeiras = []
        file_name = '../files/'+ str(self.__bairro_nome) + '.csv'

        data = csv.reader(open(file_name, 'r'))

        for rows in data:
            list_lixeiras.append(tuple(rows))

        return list_lixeiras
