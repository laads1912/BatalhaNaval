from entidade.embarcacao import Embarcacao
from entidade.bote import Bote
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from entidade.submarino import Submarino


class Oceano:
    def __init__(self, tamanho_oceano: int):
        self.__tamanho_oceano = tamanho_oceano
        self.__posicoes_barcos = {Bote(1): ["A1"], Bote(1): ["A2"], Bote(1): ["A3"], Submarino(2): ["B1", "B2"],  Submarino(2): ["B3", "B4"], Fragata(3): ["C1", "C2", "C3"],  Fragata(3): ["C4", "C5", "C6"], PortaAvioes(4): ["D1","D2","D3","D4"]}
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
    
    def add_tiros_realizados(self, tiro: str):
        self.tiros_realizados.append(tiro)
    
    def add_tiros_acertado(self, tiro: str):
        self.tiros_acertados.append(tiro)