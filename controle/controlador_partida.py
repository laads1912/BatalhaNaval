from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
from entidade.oceano import Oceano
from controle.controlador_sistema import ControladorSistema


class ControladorPartida:

    def __init__(self, controlador_sistema):
        self.__jogador = Jogador("a", "b")
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__pontuacao_total = 0
        self.__dict_posicao = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                               'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                               'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    def iniciar_partida(self):
        dados = self.__tela_partida.iniciar_partida()
        self.__jogador = self.__controlador_sistema.controlador_jogador().pega_jogador_pelo_nome(dados["nome"])
        tamanho_oceano = int(dados["tamanho_oceano"])
        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
            self.__partida = Partida(self.__jogador, tamanho_oceano)
            self.add_embarcacoes()

    def pontuacao_total(self):
        self.__tela_partida.mostrar_mensagem("Sua pontuacao é: " + str(self.__pontuacao_total) + " pontos")

    def add_embarcacoes(self):
        while True:
            contador = 0
            if contador == 8:
                break
            if contador <= 2:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Bote")
                    if len(posicoes) == 2 and posicoes[0].isalpha() and posicoes[1].isdigit():
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                        break
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida está no formato errado.")
                contador = contador + 1
            elif contador <= 4:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos("Submarino").split()]
                if len(posicoes) == 2:
                    condicao = True
                    for posicao in posicoes:
                        if posicao[0].isalpha() and posicao[1].isdigit():
                            condicao = True
                        else:
                            condicao = False
                            break
                contador = contador + 1
            elif contador <= 6:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos("Fragata").split()]
                self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                contador = contador + 1
            else:
                posicoes = [int(x) for x in self.__tela_partida.posicionar_barcos("PortaAvioes").split()]
                self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                contador = contador + 1

    def atirar(self):
        dados = self.__tela_partida.atirar()
        self.__tiros_realizados.append(dados)
        dados = list(dados)
        posicao = [self.__dict_posicao[dados[0]], int(dados[1])]