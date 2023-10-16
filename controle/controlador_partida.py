from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
from entidade.oceano import Oceano


class ControladorPartida:

    def __init__(self, controlador_sistema):
        self.__final_partida = "1"
        self.__jogador = Jogador("a", "b", "c")
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__tiros_realizados = []
        self.__dict_posicao = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                               'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def iniciar_partida(self):
        while True:
            dados = self.__tela_partida.iniciar_partida()
            self.__jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_pelo_nome(dados["nome"])
            if self.__jogador is not None:
                if self.__jogador.senha == dados["senha"]:
                    tamanho_oceano = int(dados["tamanho_oceano"])
                    if 10 >= tamanho_oceano >= 5:
                        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
                            self.__partida = Partida(self.__jogador, tamanho_oceano)
                            self.add_embarcacoes()
                            self.continuar_partida()
                            break
                    else:
                        self.__tela_partida.mostrar_mensagem("Tamanho do oceano inválido.")
                        return
                else:
                    self.__tela_partida.mostrar_mensagem("Senha inválida.")
                    return
            else:
                self.__tela_partida.mostrar_mensagem("Jogador não encontrado")
                return

    def continuar_partida(self):
        while self.__final_partida != "0":
            self.mostrar_oceano("JOGADOR")
            self.mostrar_oceano("MAQUINA")
            self.atirar()

    def pontuacao_total(self):
        self.__tela_partida.mostrar_mensagem("Sua pontuacao é: " + str(self.__partida.pontuacao) + " pontos")

    def atirar(self):
        dados = self.__tela_partida.atirar().upper()
        while True:
            if len(dados) == 2 and dados[0].upper().isalpha and dados[1].isalnum():
                tiros_realizados = self.__partida.oceano_jogador.tiros_realizados
                if dados in tiros_realizados:
                        self.__tela_partida.mostrar_mensagem("Você já atirou nessa posição")
                        return
                break

            else:
                self.__tela_partida.mostrar_mensagem("Valor inválido")
                dados = self.__tela_partida.atirar()
        self.__partida.oceano_jogador.add_tiros_realizados(dados)
        posicao_str = dados
        dados = list(dados)
        posicao = [self.__dict_posicao[dados[0]], int(dados[1])]
        matriz = self.__partida.pegar_matriz_oceano_maquina()
        posicao_barcos_maquina = self.__partida.oceano_maquina.posicoes_barcos
        matriz[posicao[0]][posicao[1]] = "X"
        nome_barco = ""
        for barco, lista_posicao in posicao_barcos_maquina.items():
            if posicao_str in lista_posicao:
                nome_barco = barco.nome

        if nome_barco == "bote":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Bote")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(4)
            matriz[posicao[0]][posicao[1]] = "B"
            self.atirar()
        elif nome_barco == "submarino":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Submarino")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "S"
            self.atirar()
        elif nome_barco == "fragata":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Fragata")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "F"
            self.atirar()
        elif nome_barco == "porta_avioes":
            self.__tela_partida.mostrar_mensagem("Você Acertou um Porta-Aviões")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "P"
            self.atirar()
        else:
            self.__tela_partida.mostrar_mensagem("Errou")
            self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)

    def mostrar_oceano(self, nome):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        if nome == "JOGADOR":
            matriz = self.__partida.pegar_matriz_oceano_jogador()
        else:
            matriz = self.__partida.pegar_matriz_oceano_maquina()
        self.__tela_partida.mostrar_legenda_oceano(nome)
        self.__tela_partida.mostrar_espaco()
        contador = 0
        while contador < self.__partida.oceano_jogador.tamanho_oceano:
            self.__tela_partida.mostrar_coordenada(contador)
            contador += 1
        self.__tela_partida.mostrar_mensagem("")
        contador = 0
        for linha in matriz:
            self.__tela_partida.mostrar_linha(dicionario[contador], linha)
            contador += 1

    def add_bote(self):
        contador = 0
        while True:
            if contador == 3:
                break
            else:
                while True:
                    posicoes = self.__tela_partida.posicionar_barcos("Bote").upper()
                    if len(posicoes) == 2 and posicoes[0].isalpha() and posicoes[1].isdigit():
                        if self.__dict_posicao[posicoes[0]] >= self.__partida.oceano_jogador.tamanho_oceano or int(
                                posicoes[1]) >= self.__partida.oceano_jogador.tamanho_oceano:
                            self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                        else:
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
                                if self.__dict_posicao[
                                     posicao[0]] >= self.__partida.oceano_jogador.tamanho_oceano or int(
                                     posicao[1]) >= self.__partida.oceano_jogador.tamanho_oceano:
                                    condicao = False
                                    break
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
                                if self.__dict_posicao[
                                     posicao[0]] >= self.__partida.oceano_jogador.tamanho_oceano or int(
                                     posicao[1]) >= self.__partida.oceano_jogador.tamanho_oceano:
                                    condicao = False
                                    break
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
                        if self.__dict_posicao[
                             posicao[0]] >= self.__partida.oceano_jogador.tamanho_oceano or int(
                             posicao[1]) >= self.__partida.oceano_jogador.tamanho_oceano:
                            condicao = False
                            break
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
        self.mostrar_oceano("JOGADOR")
        self.add_bote()
        self.mostrar_oceano("JOGADOR")
        self.add_submarino()
        self.mostrar_oceano("JOGADOR")
        self.add_fragata()
        self.mostrar_oceano("JOGADOR")
        self.add_porta_avioes()
