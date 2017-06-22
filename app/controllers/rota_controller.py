# -*- coding: utf-8 -*-
from models.rota import *
from dao.dao_clientes import *

class RotaController(object):

    """docstring for RotaController."""
    def __init__(self):
        pass

    def calcular_rota(self, bairro):
        rota = Rota(bairro)
        dao_c = DaoClientes(bairro)
        list_coleta = dao_c.get_clientes_interessados()
        
        if len(list_coleta) <= 0:
            return rota.gerar_rota_padrao()

        return rota.gerar_rota_personalizada(list_coleta)