from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
from entidade.oceano import Oceano


class ControladorPartida:

    def __init__(self, controlador_sistema):
        self.__jogador = Jogador("a", "b")
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__pontuacao_total = 0
        self.__dict_posicao = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                               'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

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
        contador = 0
        while True:
            if contador == 8:
                break
            if contador <= 2:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Bote")
                    if len(posicoes) == 2 and posicoes[0].isalpha() and posicoes[1].isdigit():
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                        break
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                contador += 1
            elif contador <= 4:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Submarino").split()
                    if len(posicoes) == 2:
                        condicao = True
                        for posicao in posicoes:
                            if posicao[0].isalpha() and posicao[1].isdigit():
                                condicao = True
                            else:
                                condicao = False
                                break
                        if condicao:
                            posicao1 = posicoes[0]
                            posicao2 = posicoes[1]
                            if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
                               abs(int(posicao1[1]) - int(posicao2[1])) <= 1:
                                self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                                break
                            else:
                                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                contador += 1
            elif contador <= 6:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Fragata").split()
                    if len(posicoes) == 3:
                        condicao = True
                        for posicao in posicoes:
                            if posicao[0].isalpha() and posicao[1].isdigit():
                                condicao = True
                            else:
                                condicao = False
                                break
                        if condicao:
                            posicao1 = posicoes[0]
                            posicao2 = posicoes[1]
                            posicao3 = posicoes[2]
                            if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
                               abs(int(posicao1[1]) - int(posicao2[1])) <= 1 and \
                               abs(self.__dict_posicao[posicao2[0]] - self.__dict_posicao[posicao3[0]]) <= 1 and \
                               abs(int(posicao2[1]) - int(posicao3[1])) <= 1 and \
                               (posicao1[0] == posicao2[0] == posicao3[0] or posicao1[1] == posicao2[1] == posicao3[1]):
                                self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                                break
                            else:
                                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                contador += 1
            else:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("PortaAvioes").split()
                    if len(posicoes) == 4:
                        condicao = True
                        for posicao in posicoes:
                            if posicao[0].isalpha() and posicao[1].isdigit():
                                condicao = True
                            else:
                                condicao = False
                                break
                        if condicao:
                            posicao1 = posicoes[0]
                            posicao2 = posicoes[1]
                            posicao3 = posicoes[2]
                            posicao4 = posicoes[3]
                            if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
                               abs(int(posicao1[1]) - int(posicao2[1])) <= 1 and \
                               abs(self.__dict_posicao[posicao2[0]] - self.__dict_posicao[posicao3[0]]) <= 1 and \
                               abs(int(posicao2[1]) - int(posicao3[1])) <= 1 and \
                               abs(self.__dict_posicao[posicao3[0]] - self.__dict_posicao[posicao4[0]]) <= 1 and \
                               abs(int(posicao3[1]) - int(posicao4[1])) <= 1 and \
                               (posicao1[0] == posicao2[0] == posicao3[0] == posicao4[0] or
                               posicao1[1] == posicao2[1] == posicao3[1] == posicao4[1]):
                                self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                                break
                            else:
                                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                contador += 1

    def atirar(self):
        dados = self.__tela_partida.atirar()
        self.__tiros_realizados.append(dados)
        dados = list(dados)
        posicao = [self.__dict_posicao[dados[0]], int(dados[1])]
