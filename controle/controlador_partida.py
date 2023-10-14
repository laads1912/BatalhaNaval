from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
from entidade.oceano import Oceano


class ControladorPartida:

    def __init__(self, controlador_sistema):
        self.__final_partida = "1"
        self.__jogador = Jogador("a", "b")
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__tiros_realizados = []
        self.__dict_posicao = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                               'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    def abre_tela(self):
        lista_opcoes = {1: self.iniciar_partida, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_partida.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                raise ValueError
            except ValueError:
                self.__tela_partida.mostrar_mensagem("Valor inválido, digite um número Válido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def iniciar_partida(self):
        dados = self.__tela_partida.iniciar_partida()
        self.__jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_pelo_nome(dados["nome"])
        tamanho_oceano = int(dados["tamanho_oceano"])
        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
            self.__partida = Partida(self.__jogador, tamanho_oceano)
            self.add_embarcacoes()
            self.continuar_partida()

    def continuar_partida(self):
        while self.__final_partida == "0":
            self.mostrar_oceano_jogador()
            self.mostrar_oceano_maquina()
            self.atirar()


    def pontuacao_total(self):
        self.__tela_partida.mostrar_mensagem("Sua pontuacao é: " + str(self.__partida.pontuacao) + " pontos")

    def atirar(self):
        dados = self.__tela_partida.atirar()
        while True:
            if len(dados) == 2 and dados[0].upper().isalpha and dados[1].isalnum():
                tiros_realizados = self.__partida.oceano_jogador.tiros_realizados()
                for tiro in tiros_realizados:
                    if tiro == dados:
                        self.__tela_partida.mostrar_mensagem("Você já atirou nessa posição")
                        dados = self.__tela_partida.atirar()
                        return          
                break
            
            else:
                self.__tela_partida.mostrar_mensagem("Valor inválido")
                dados = self.__tela_partida.atirar()
                return          
        self.__partida.oceano_jogador.add_tiros_realizados(dados)
        posicao_str = dados
        dados = list(dados)
        posicao = [self.__dict_posicao[dados[0]], int(dados[1])]
        matriz = self.__partida.pegar_matriz_oceano_maquina()
        posicao_tiro_matriz = matriz[posicao[0]][posicao[1]]
        if posicao_tiro_matriz == "B":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Barco")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(4)
            matriz[posicao[0]][posicao[1]] = "O"
            self.atirar()
        elif posicao_tiro_matriz == "S":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Submarino")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)            
            matriz[posicao[0]][posicao[1]] = "O"
            self.atirar()
        elif posicao_tiro_matriz == "F":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Fragata")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "O"
            self.atirar()
        elif posicao_tiro_matriz == "P":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Porta-Aviões")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "O"
            self.atirar()
        else:
            self.__tela_partida.mostrar_mensagem("Errou")
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)

    
    def mostrar_oceano_jogador(self):
        contador = 0
        matriz = self.__partida.pegar_matriz_oceano_jogador()
        self.__tela_partida.mostrar_legenda_oceano("JOGADOR")
        self.__tela_partida.mostrar_mensagem("  12345678910")
        for linha in matriz:
            self.__tela_partida.mostrar_mensagem(self.__dict_posicao[contador] + linha)

    def mostrar_oceano_maquina(self):
        contador = 0
        matriz = self.__partida.pegar_matriz_oceano_maquina()
        self.__tela_partida.mostrar_legenda_oceano("MAQUINA")
        self.__tela_partida.mostrar_mensagem("  12345678910")
        for linha in matriz:
            self.__tela_partida.mostrar_mensagem(self.__dict_posicao[contador] + linha)


    def add_bote(self):
        contador = 0
        while True:
            if contador == 3:
                break
            else:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Bote").upper()
                    if len(posicoes) == 2 and posicoes[0].isalpha() and posicoes[1].isdigit():
                        posicao_ocupada = False
                        for posicao in self.__partida.oceano_jogador.posicoes_barcos.values():
                            if posicao == posicoes:
                                posicao_ocupada = True
                        if posicao_ocupada:
                            self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
                        else:
                            self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                            break
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
            contador += 1

    def add_submarino(self):
        contador = 3
        while True:
            if contador == 5:
                break
            else:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Submarino").upper().split()
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
                                posicao_ocupada = False
                                for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                                    if posicao1 in posicoes2 or posicao2 in posicoes2:
                                        posicao_ocupada = True
                                if posicao_ocupada:
                                    self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
                                else:
                                    self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador],
                                                                    posicoes)
                                    break
                            else:
                                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
            contador += 1

    def add_fragata(self):
        contador = 5
        while True:
            if contador == 7:
                break
            else:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Fragata").upper().split()
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
                                    (posicao1[0] == posicao2[0] == posicao3[0] or posicao1[1] == posicao2[1] ==
                                     posicao3[1]):
                                posicao_ocupada = False
                                for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                                    if posicao1 in posicoes2 or posicao2 in posicoes2:
                                        posicao_ocupada = True
                                if posicao_ocupada:
                                    self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
                                else:
                                    self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador],
                                                                    posicoes)
                                    break
                            else:
                                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
            contador += 1

    def add_porta_avioes(self):
        while True:
            posicoes = self.__tela_partida.posicionar_barcos("PortaAvioes").upper().split()
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
                        posicao_ocupada = False
                        for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                            if posicao1 in posicoes2 or posicao2 in posicoes2:
                                posicao_ocupada = True
                        if posicao_ocupada:
                            self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
                        else:
                            self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[7],
                                                            posicoes)
                            break
                    else:
                        self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                else:
                    self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
            else:
                self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")

    def add_embarcacoes(self):
        self.mostrar_oceano_jogador()
        self.add_bote()
        self.mostrar_oceano_jogador()
        self.add_submarino()
        self.mostrar_oceano_jogador()
        self.add_fragata()
        self.mostrar_oceano_jogador()
        self.add_porta_avioes()

    # def add_embarcacoes(self):
    #     contador = 0
    #     while True:
    #         if contador == 8:
    #             break
    #         if contador <= 2:
    #             # adicionar bote ao oceano
    #             while True:
    #                 posicoes = self.__tela_partida.posicionar_barcos("Bote")
    #                 if len(posicoes) == 2 and posicoes[0].isalpha() and posicoes[1].isdigit():
    #                     posicao_ocupada = False
    #                     for posicao in self.__partida.oceano_jogador.posicoes_barcos.values():
    #                         if posicao == posicoes:
    #                             posicao_ocupada = True
    #                     if posicao_ocupada:
    #                         self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
    #                     else:
    #                         self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
    #                         break
    #                 else:
    #                     self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #             contador += 1
    #         elif contador <= 4:
    #             # adicionar submarino ao oceano
    #             while True:
    #                 posicoes = self.__tela_partida.posicionar_barcos("Submarino").split()
    #                 if len(posicoes) == 2:
    #                     condicao = True
    #                     for posicao in posicoes:
    #                         if posicao[0].isalpha() and posicao[1].isdigit():
    #                             condicao = True
    #                         else:
    #                             condicao = False
    #                             break
    #                     if condicao:
    #                         posicao1 = posicoes[0]
    #                         posicao2 = posicoes[1]
    #                         if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
    #                                 abs(int(posicao1[1]) - int(posicao2[1])) <= 1:
    #                             posicao_ocupada = False
    #                             for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
    #                                 if posicao1 in posicoes2 or posicao2 in posicoes2:
    #                                     posicao_ocupada = True
    #                             if posicao_ocupada:
    #                                 self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
    #                             else:
    #                                 self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador],
    #                                                                 posicoes)
    #                                 break
    #                         else:
    #                             self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                     else:
    #                         self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                 else:
    #                     self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #             contador += 1
    #         elif contador <= 6:
    #             # adicionar fragata ao oceano
    #             while True:
    #                 posicoes = self.__tela_partida.posicionar_barcos("Fragata").split()
    #                 if len(posicoes) == 3:
    #                     condicao = True
    #                     for posicao in posicoes:
    #                         if posicao[0].isalpha() and posicao[1].isdigit():
    #                             condicao = True
    #                         else:
    #                             condicao = False
    #                             break
    #                     if condicao:
    #                         posicao1 = posicoes[0]
    #                         posicao2 = posicoes[1]
    #                         posicao3 = posicoes[2]
    #                         if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
    #                                 abs(int(posicao1[1]) - int(posicao2[1])) <= 1 and \
    #                                 abs(self.__dict_posicao[posicao2[0]] - self.__dict_posicao[posicao3[0]]) <= 1 and \
    #                                 abs(int(posicao2[1]) - int(posicao3[1])) <= 1 and \
    #                                 (posicao1[0] == posicao2[0] == posicao3[0] or posicao1[1] == posicao2[1] ==
    #                                  posicao3[1]):
    #                             posicao_ocupada = False
    #                             for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
    #                                 if posicao1 in posicoes2 or posicao2 in posicoes2:
    #                                     posicao_ocupada = True
    #                             if posicao_ocupada:
    #                                 self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
    #                             else:
    #                                 self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador],
    #                                                                 posicoes)
    #                                 break
    #                         else:
    #                             self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                     else:
    #                         self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                 else:
    #                     self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #             contador += 1
    #         else:
    #             # adicionar porta avioes ao oceano
    #             while True:
    #                 posicoes = self.__tela_partida.posicionar_barcos("PortaAvioes").split()
    #                 if len(posicoes) == 4:
    #                     condicao = True
    #                     for posicao in posicoes:
    #                         if posicao[0].isalpha() and posicao[1].isdigit():
    #                             condicao = True
    #                         else:
    #                             condicao = False
    #                             break
    #                     if condicao:
    #                         posicao1 = posicoes[0]
    #                         posicao2 = posicoes[1]
    #                         posicao3 = posicoes[2]
    #                         posicao4 = posicoes[3]
    #                         if abs(self.__dict_posicao[posicao1[0]] - self.__dict_posicao[posicao2[0]]) <= 1 and \
    #                                 abs(int(posicao1[1]) - int(posicao2[1])) <= 1 and \
    #                                 abs(self.__dict_posicao[posicao2[0]] - self.__dict_posicao[posicao3[0]]) <= 1 and \
    #                                 abs(int(posicao2[1]) - int(posicao3[1])) <= 1 and \
    #                                 abs(self.__dict_posicao[posicao3[0]] - self.__dict_posicao[posicao4[0]]) <= 1 and \
    #                                 abs(int(posicao3[1]) - int(posicao4[1])) <= 1 and \
    #                                 (posicao1[0] == posicao2[0] == posicao3[0] == posicao4[0] or
    #                                  posicao1[1] == posicao2[1] == posicao3[1] == posicao4[1]):
    #                             posicao_ocupada = False
    #                             for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
    #                                 if posicao1 in posicoes2 or posicao2 in posicoes2:
    #                                     posicao_ocupada = True
    #                             if posicao_ocupada:
    #                                 self.__tela_partida.mostrar_mensagem("Posicão ocupada.")
    #                             else:
    #                                 self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador],
    #                                                                 posicoes)
    #                                 break
    #                         else:
    #                             self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                     else:
    #                         self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #                 else:
    #                     self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
    #             contador += 1