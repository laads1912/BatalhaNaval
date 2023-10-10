from entidade.oceano import Oceano
from entidade.bote import Bote
from entidade.fragata import Fragata
from entidade.porta_avioes import PortaAvioes
from entidade.submarino import Submarino


class Partida:
    def __init__(self, jogador, tamanho_oceano: int):
        self.__bote1_maquina = Bote(1)
        self.__bote2_maquina = Bote(1)
        self.__bote3_maquina = Bote(1)
        self.__submarino1_maquina = Submarino(2)
        self.__submarino2_maquina = Submarino(2)
        self.__fragata1_maquina = Fragata(3)
        self.__fragata2_maquina = Fragata(3)
        self.__porta_avioes_maquina = PortaAvioes(4)

        self.__bote1_jogador = Bote(1)
        self.__bote2_jogador = Bote(1)
        self.__bote3_jogador = Bote(1)
        self.__submarino1_jogador = Submarino(2)
        self.__submarino2_jogador = Submarino(2)
        self.__fragata1_jogador = Fragata(3)
        self.__fragata2_jogador = Fragata(3)
        self.__porta_avioes_jogador = PortaAvioes(4)

        self.__embarcacoes_jogador = [self.__bote1_jogador,
                                      self.__bote2_jogador,
                                      self.__bote3_jogador,
                                      self.__submarino1_jogador,
                                      self.__submarino2_jogador,
                                      self.__fragata1_jogador,
                                      self.__fragata2_jogador,
                                      self.__porta_avioes_jogador]
        self.__embarcacoes_maquina = [self.__bote1_maquina,
                                      self.__bote2_maquina,
                                      self.__bote3_maquina,
                                      self.__submarino1_maquina,
                                      self.__submarino2_maquina,
                                      self.__fragata1_maquina,
                                      self.__fragata2_maquina,
                                      self.__porta_avioes_maquina]
        self.__oceano_jogador = Oceano(tamanho_oceano)
        self.__oceano_maquina = Oceano(tamanho_oceano)
        
        self.__pontuacao = 0
        self.__jogador = jogador

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador

    @property
    def embarcacoes_jogador(self):
        return self.__embarcacoes_jogador

    def add_barco_oceano(self, barco, posicoes):
        self.__oceano_jogador.add_barco(barco, posicoes)

    def pegar_matriz_oceano_jogador(self):
        return self.__oceano_jogador.pegar_matriz()