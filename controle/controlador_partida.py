from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador

class ControladorPartida():

    def __init__(self, controlador_sistema):
        self.__partidas = []
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema

    def iniciar_partida(self, jogador):
        if (isinstance(jogador, Jogador)):
            self.__partida = Partida(jogador)
            self.__partidas.append(self.__partida)
    
    def add_partida(self, partida: Partida):
        if (isinstance(partida, Partida)):
            self.__partidas.append(partida)
        else:
            self.__tela_partida.mensagem("Isso não é uma Partida válida")