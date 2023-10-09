from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
from entidade.oceano import Oceano
from controle.controlador_sistema import ControladorSistema

class ControladorPartida():

    def __init__(self, controlador_sistema): 
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__pontuacao_total = 0
        

    def iniciar_partida(self):
        dados = self.__tela_partida.iniciar_partida()
        self.__jogador = self.__controlador_sistema.controlador_jogador().pega_jogador_pelo_nome(dados["nome"])
        tamanho_oceano = int(dados["tamanho_oceano"])
        if (isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int)):
            self.__partida = Partida(self.__jogador, tamanho_oceano)


    def pontuacao_total(self):
        self.__tela_partida.mostrar_mensagem("Sua pontuacao é: " + self.__pontuacao_total + "pontos")

    def add_embarcacoes(self):
        while True:
            contador = 0
            if contador == 8:
                break
            if contador <= 2:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos().split()]
                self.__partida.__oceano_jogador.posicoes_barcos[contador] = posicoes
            elif contador <= 4:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos().split()]
                self.__partida.__oceano_jogador.posicoes_barcos[contador] = posicoes
            elif contador <= 6:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos().split()]
                self.__partida.__oceano_jogador.posicoes_barcos[contador] = posicoes            
            else:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos().split()]
                self.__partida.__oceano_jogador.posicoes_barcos[contador] = posicoes    