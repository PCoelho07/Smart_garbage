# -*- coding: utf-8 -*-
from app.models.rota import *

class RotaController(object):

    """docstring for RotaController."""
    def __init__(self):
        pass

    def calcular_rota(self, bairro):
        rota = Rota(bairro)

        return rota.gerar_rota_personalizada(lista_coleta)
