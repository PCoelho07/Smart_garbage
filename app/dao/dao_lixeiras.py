# -*- coding: utf-8 -*-
import csv
from app.models.lixeira import *
from app.models.bairro import *

class DaoLixeiras(object):

    """docstring for DaoLixeiras."""
    def __init__(self, bairro = Bairro):
        self.__bairro_nome = bairro.get_nome()


    def get_lixeiras_from_csv(self):
        list_lixeiras = []
        file_name = '../files/'+ str(self.__bairro_nome) + '.csv'

        data = csv.reader(open(file_name, 'r'))

        for rows in data:
            lixeira = Lixeira(rows[0], rows[1], rows[2])
            list_lixeiras.append(lixeira)

        return list_lixeiras
