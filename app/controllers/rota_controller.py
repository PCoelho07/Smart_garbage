# -*- coding: utf-8 -*-
from app.models.rota import *

class RotaController(object):

    """docstring for RotaController."""
    def __init__(self):
        pass

    def calcular_rota(self, bairro, lista_coleta = ''):
        rota = Rota(bairro)

        if lista_coleta == '':
            return rota.gerar_rota_padrao()

        return rota.gerar_rota_personalizada(lista_coleta)
