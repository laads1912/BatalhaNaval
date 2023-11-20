from limite.tela_sistema import TelaSistema
from controle.controlador_partida import ControladorPartida
from controle.controlador_jogador import ControladorJogador


class ControladorSistema:

    def __init__(self):
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastrar_partida(self):
        self.__controlador_partida.iniciar_partida()

    def cadastrar_jogador(self):
        self.__controlador_jogador.abre_tela()

    def partida_teste(self):
        self.__controlador_partida.partida_teste()

    def finaliza_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_partida, 2: self.cadastrar_jogador, 0: self.finaliza_sistema, 123: self.partida_teste}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            if opcao_escolhida == "":
                self.__tela_sistema.mostrar_mensagem("Opção inválida")
            elif int(opcao_escolhida) in lista_opcoes:
                opcao_escolhida = int(opcao_escolhida)
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_sistema.mostrar_mensagem("Opção inválida")
