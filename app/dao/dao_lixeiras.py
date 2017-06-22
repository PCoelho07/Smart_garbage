# -*- coding: utf-8 -*-
import csv
from models.lixeira import *
from models.bairro import *

class DaoLixeiras(object):

    """docstring for DaoLixeiras."""
    def __init__(self, bairro = None):
        self.__bairro = bairro
        self.__file_name = ''

        if bairro is not None:
            self.__file_name = self.__bairro.get_nome()



    def get_lixeiras_from_csv(self):
        list_lixeiras = []
        file_path = 'app/files/'+ str(self.__file_name) + '.csv'

        data = csv.reader(open(file_path, 'r'))

        for rows in data:
            lixeira = Lixeira(rows[0], rows[1], rows[2])
            list_lixeiras.append(lixeira)

        return list_lixeiras
