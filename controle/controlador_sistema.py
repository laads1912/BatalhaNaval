from limite.tela_sistema import TelaSistema
from controle.controlador_partida import ControladorPartida
from controle.controlador_jogador import ControladorJogador
from controle.controlador_oceano import ControladorOceano

class ControladorSistema:

    def __init__(self):
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_oceano = ControladorOceano(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastrar_partida(self):
        self.__controlador_partida.abre_tela()

    def cadastrar_jogador(self):
        self.__controlador_jogador.abre_tela()

    def cadastrar_oceano(self):
        self.__controlador_oceano.abre_tela()
    
    def finaliza_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_jogador, 0: self.finaliza_sistema}
        
        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela.mensagem("Valor inválido, digite um número Válido")