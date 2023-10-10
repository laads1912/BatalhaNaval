from entidade.embarcacao import Embarcacao
from entidade.bote import Bote
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from entidade.submarino import Submarino


class Oceano:
    def __init__(self, tamanho_oceano: int):
        self.__tamanho_oceano = tamanho_oceano
        self.__posicoes_barcos = {}
        self.__tiros_realizados = []
        self.__tiros_acertados = []

    @property
    def tamanho_oceano(self):
        return self.__tamanho_oceano

    @property
    def posicoes_barcos(self):
        return self.__posicoes_barcos

    @property
    def tiros_realizados(self):
        return self.__tiros_realizados

    @property
    def tiros_acertados(self):
        return self.__tiros_acertados

    def add_barco(self, barco, posicoes):
        self.__posicoes_barcos[barco] = posicoes
