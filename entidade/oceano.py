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
        self.__matriz_oceano = [["~"] * self.__tamanho_oceano for _ in range(self.__tamanho_oceano)]

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
        dicionario = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                      'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                      'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        self.__posicoes_barcos[barco] = posicoes
        if isinstance(posicoes, str):
            self.__matriz_oceano[dicionario[posicoes[0]]][int(posicoes[1])] = "B"
        else:
            for posicao in posicoes:
                if isinstance(barco, Submarino):
                    self.__matriz_oceano[dicionario[posicao[0]]][int(posicao[1])] = "S"
                elif isinstance(barco, Fragata):
                    self.__matriz_oceano[dicionario[posicao[0]]][int(posicao[1])] = "F"
                else:
                    self.__matriz_oceano[dicionario[posicao[0]]][int(posicao[1])] = "P"

    def pegar_matriz(self):
        return self.__matriz_oceano