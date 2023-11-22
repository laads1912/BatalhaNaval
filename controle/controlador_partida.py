from entidade.partida import Partida
from limite.tela_partida import TelaPartida
from entidade.jogador import Jogador
import random


class ControladorPartida:

    def __init__(self, controlador_sistema):
        self.__final_partida = "1"
        self.__jogada = "1"
        self.__jogador = Jogador("a", "b", "c")
        self.__partida = Partida(self.__jogador, 1)
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__dict_posicao = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                               'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    def iniciar_partida(self):
        while True:
            dados = self.__tela_partida.iniciar_partida()
            if dados is None:
                self.__controlador_sistema.abre_tela()
            self.__jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_pelo_nome(dados["nome"])
            if self.__jogador is None:
                self.__tela_partida.mostrar_mensagem("Esse jogador não está cadastrado, favor verifique os jogadores "
                                                     "cadastrados!")
                self.__controlador_sistema.abre_tela()
                return
            if self.__jogador is not None:
                if self.__jogador.senha == dados["senha"]:
                    tamanho_oceano = int(dados["tamanho_oceano"])
                    if 10 >= tamanho_oceano >= 7:
                        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
                            self.__partida = Partida(self.__jogador, tamanho_oceano)
                            self.add_embarcacoes()
                            self.add_embarcacoes_maquina()
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
        while True:
            if self.__final_partida == "0":
                self.__jogador.add_partida(self.__partida)
                self.__jogador.add_pontuacao(self.__partida.pontuacao)
                self.__final_partida = "1"
                return self.__controlador_sistema.abre_tela()
            if self.__jogada == "1":
                self.mostrar_oceano("JOGADOR")
                self.mostrar_oceano("MAQUINA")
                self.atirar()
            else:
                self.atirar_maquina()

    def pontuacao_total(self):
        self.__tela_partida.mostrar_mensagem("Sua pontuacao é: " + str(self.__partida.pontuacao) + " pontos")

    def atirar(self):
        dados = self.__tela_partida.atirar().upper()
        while True:
            if len(dados) == 2 and dados[0].isalpha and dados[1].isdigit():
                if dados[0].isdigit():
                    self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    return
                elif self.__dict_posicao[dados[0]] >= self.__partida.oceano_jogador.tamanho_oceano or int(
                        dados[1]) >= self.__partida.oceano_jogador.tamanho_oceano:
                    self.__tela_partida.mostrar_mensagem("Posição fornecida é inválida.")
                    return
                tiros_realizados = self.__partida.oceano_jogador.tiros_realizados
                if dados in tiros_realizados:
                    self.__tela_partida.mostrar_mensagem("Você já atirou nessa posição")
                    return
                break
            else:
                self.__tela_partida.mostrar_mensagem("Valor inválido")
                dados = self.__tela_partida.atirar().upper()
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
                if nome_barco != "bote":
                    lista_posicao.remove(posicao_str)
                if len(lista_posicao) == 0:
                    self.__partida.add_pontuacao(3)

        if nome_barco == "bote":
            self.__partida.add_contador()
            self.__tela_partida.mostrar_mensagem("VOCÊ ACERTOU UM BOTE!")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(4)
            matriz[posicao[0]][posicao[1]] = "B"
            if self.__partida.contador == 17:
                self.__tela_partida.mostrar_mensagem("Você Ganhou!")
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.mostrar_oceano("MAQUINA")
            self.atirar()

        elif nome_barco == "submarino":
            self.__partida.add_contador()
            self.__tela_partida.mostrar_mensagem("VOCÊ ACERTOU UM SUBMARINO!")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "S"
            if self.__partida.contador == 17:
                self.__tela_partida.mostrar_mensagem("Você Ganhou!")
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.mostrar_oceano("MAQUINA")
            self.atirar()

        elif nome_barco == "fragata":
            self.__partida.add_contador()
            self.__tela_partida.mostrar_mensagem("VOCÊ ACERTOU UMA FRAGATA!")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "F"
            if self.__partida.contador == 17:
                self.__tela_partida.mostrar_mensagem("Você Ganhou!")
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.mostrar_oceano("MAQUINA")
            self.atirar()

        elif nome_barco == "porta_avioes":
            self.__partida.add_contador()
            self.__tela_partida.mostrar_mensagem("VOCÊ ACERTOU UM PORTA-AVIÕES!")
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "P"
            if self.__partida.contador == 17:
                self.__tela_partida.mostrar_mensagem("Você Ganhou!")
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.mostrar_oceano("MAQUINA")
            self.atirar()

        else:
            self.__tela_partida.mostrar_mensagem("ERROU!!")
            self.__jogada = "0"

    def mostrar_oceano_add_embarcacoes(self, barco):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        matriz = self.__partida.pegar_matriz_oceano_jogador()
        oceano = """"""
        oceano += '~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE TIRO EM ALGUM NAVIO\n'
        oceano += "\n"
        oceano += "----- OCEANO JOGADOR -----\n"
        oceano += "\n"
        oceano += "SUA PONTUAÇÃO É: " + str(self.__partida.pontuacao) + "\n"
        oceano += "\n"
        contador = 0
        oceano += "    "
        while contador < self.__partida.oceano_jogador.tamanho_oceano:
            oceano += str(contador) + " "
            contador += 1
        oceano += "\n"
        contador = 0
        for linha in matriz:
            oceano += f'{dicionario[contador]} {" ".join(linha)}\n'
            contador += 1
        oceano += "\n"
        dados = self.__tela_partida.mostrar_oceano_add_embarcacoes(oceano, barco)
        return dados

    def mostrar_oceano(self, nome):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        oceano = """"""
        if nome == "JOGADOR":
            matriz = self.__partida.pegar_matriz_oceano_jogador()
            oceano += '~ = OCEANO   x = TIRO    B = BOTE    S = SUBMARINO   F = FRAGATA     P = PORTA-AVIÕES    O = ACERTO DE TIRO EM ALGUM NAVIO\n'
            oceano += "\n"
            oceano += "----- OCEANO JOGADOR -----\n"
            oceano += "\n"
            oceano += "SUA PONTUAÇÃO É: " + str(self.__partida.pontuacao) + "\n"
            oceano += "\n"
        else:
            matriz = self.__partida.pegar_matriz_oceano_maquina()
            oceano += "\n"
            oceano += "OCEANO MÁQUINA\n"
            oceano += "\n"
        contador = 0
        oceano += "    "
        while contador < self.__partida.oceano_jogador.tamanho_oceano:
            oceano += str(contador) + " "
            contador += 1
        oceano += "\n"
        contador = 0
        for linha in matriz:
            oceano += f'{dicionario[contador]} {" ".join(linha)}\n'
            contador += 1
        oceano += "\n"
        self.__tela_partida.mostrar_oceano(oceano)

    def add_bote(self):
        contador = 0
        while True:
            if contador == 3:
                break
            else:
                while True:
                    dados = self.mostrar_oceano_add_embarcacoes("Bote")
                    posicoes = dados['posicao'].upper()
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
                    dados = self.mostrar_oceano_add_embarcacoes("Submarino")
                    posicoes = dados['posicao'].upper().split()
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
                    dados = self.mostrar_oceano_add_embarcacoes("Fragata")
                    posicoes = dados['posicao'].upper().split()
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
                                    if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2:
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
            dados = self.mostrar_oceano_add_embarcacoes("Porta Avioes")
            posicoes = dados['posicao'].upper().split()
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
                            if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2 or posicao4 in \
                                    posicoes2:
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
        self.add_bote()
        self.add_submarino()
        self.add_fragata()
        self.add_porta_avioes()

    def add_embarcacoes_maquina(self):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        tamanho_oceano = self.__partida.oceano_maquina.tamanho_oceano
        contador = 0
        while True:
            if contador == 8:
                return
            elif contador < 3:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 1))
                    posicao_y = random.randint(0, (tamanho_oceano - 1))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    posicao_ocupada = False
                    for posicoes in self.__partida.oceano_maquina.posicoes_barcos.values():
                        if posicao1 == posicoes:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_maquina(self.__partida.embarcacoes_maquina[contador], posicao1)
                        contador += 1
                        break
            elif contador < 5:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 2))
                    posicao_y = random.randint(0, (tamanho_oceano - 2))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                    posicoes = [posicao1, posicao2]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_maquina.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_maquina(self.__partida.embarcacoes_maquina[contador], posicoes)
                        contador += 1
                        break
            elif contador < 7:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 3))
                    posicao_y = random.randint(0, (tamanho_oceano - 3))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                        posicao3 = dicionario[posicao_x] + str(posicao_y + 2)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                        posicao3 = dicionario[posicao_x + 2] + str(posicao_y)
                    posicoes = [posicao1, posicao2, posicao3]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_maquina.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_maquina(self.__partida.embarcacoes_maquina[contador], posicoes)
                        contador += 1
                        break
            else:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 4))
                    posicao_y = random.randint(0, (tamanho_oceano - 4))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                        posicao3 = dicionario[posicao_x] + str(posicao_y + 2)
                        posicao4 = dicionario[posicao_x] + str(posicao_y + 3)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                        posicao3 = dicionario[posicao_x + 2] + str(posicao_y)
                        posicao4 = dicionario[posicao_x + 3] + str(posicao_y)
                    posicoes = [posicao1, posicao2, posicao3, posicao4]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_maquina.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2 or posicao4 in \
                                posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_maquina(self.__partida.embarcacoes_maquina[contador], posicoes)
                        contador += 1
                        break

    def atirar_maquina(self):
        tamanho_oceano = self.__partida.oceano_jogador.tamanho_oceano
        matriz_oceano_jogador = self.__partida.oceano_jogador.pegar_matriz()
        posicao_x = random.randint(0, (tamanho_oceano - 1))
        posicao_y = random.randint(0, (tamanho_oceano - 1))
        if matriz_oceano_jogador[posicao_x][posicao_y] == "B" or \
                matriz_oceano_jogador[posicao_x][posicao_y] == "S" or matriz_oceano_jogador[posicao_x][
             posicao_y] == "F" or matriz_oceano_jogador[posicao_x][posicao_y] == "P":
            matriz_oceano_jogador[posicao_x][posicao_y] = "O"
            self.__partida.add_contador_maquina()
            if self.__partida.contador_maquina == 17:
                self.__tela_partida.mostrar_mensagem("Você Perdeu!")
                self.__partida.resultado = "Derrota!"
                self.__final_partida = "0"
                return
            self.__jogada = "1"
        else:
            matriz_oceano_jogador[posicao_x][posicao_y] = "X"
            self.__jogada = "1"

    def partida_teste(self):
        while True:
            dados = self.__tela_partida.iniciar_partida()
            if dados is None:
                self.__controlador_sistema.abre_tela()
            self.__jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_pelo_nome(dados["nome"])
            if self.__jogador is None:
                self.__tela_partida.mostrar_mensagem("Esse jogador não está cadastrado, favor verifique os jogadores "
                                                     "cadastrados!")
                self.__controlador_sistema.abre_tela()
                return
            if self.__jogador is not None:
                if self.__jogador.senha == dados["senha"]:
                    tamanho_oceano = int(dados["tamanho_oceano"])
                    if 10 >= tamanho_oceano >= 7:
                        if isinstance(self.__jogador, Jogador) and isinstance(tamanho_oceano, int):
                            self.__partida = Partida(self.__jogador, tamanho_oceano)
                            self.add_embarcacoes_teste()
                            self.add_embarcacoes_maquina()
                            self.continuar_partida_teste()
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

    def continuar_partida_teste(self):
        while True:
            if self.__final_partida == "0":
                self.__jogador.add_partida(self.__partida)
                self.__jogador.add_pontuacao(self.__partida.pontuacao)
                self.__final_partida = "1"
                return self.__controlador_sistema.abre_tela()
            if self.__jogada == "1":
                self.atirar_teste()
            else:
                self.atirar_maquina()

    def atirar_teste(self):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        tamanho_oceano = self.__partida.oceano_jogador.tamanho_oceano
        posicao_x = dicionario[random.randint(0, (tamanho_oceano - 1))]
        posicao_y = random.randint(0, (tamanho_oceano - 1))
        posicao_str = posicao_x + str(posicao_y)
        self.__partida.oceano_jogador.add_tiros_realizados(posicao_str)
        dados = list(posicao_str)
        posicao = [self.__dict_posicao[dados[0]], int(dados[1])]
        matriz = self.__partida.pegar_matriz_oceano_maquina()
        posicao_barcos_maquina = self.__partida.oceano_maquina.posicoes_barcos
        matriz[posicao[0]][posicao[1]] = "X"
        nome_barco = ""
        for barco, lista_posicao in posicao_barcos_maquina.items():
            if posicao_str in lista_posicao:
                nome_barco = barco.nome
                if nome_barco != "bote":
                    lista_posicao.remove(posicao_str)
                if len(lista_posicao) == 0:
                    self.__partida.add_pontuacao(3)

        if nome_barco == "bote":
            self.__partida.add_contador()
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(4)
            matriz[posicao[0]][posicao[1]] = "B"
            if self.__partida.contador == 17:
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.atirar_teste()

        elif nome_barco == "submarino":
            self.__partida.add_contador()
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "S"
            if self.__partida.contador == 17:
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.atirar_teste()

        elif nome_barco == "fragata":
            self.__partida.add_contador()
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "F"
            if self.__partida.contador == 17:
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.atirar_teste()

        elif nome_barco == "porta_avioes":
            self.__partida.add_contador()
            self.__partida.oceano_jogador.add_tiros_acertado(posicao_str)
            self.__partida.add_pontuacao(1)
            matriz[posicao[0]][posicao[1]] = "P"
            if self.__partida.contador == 17:
                self.__partida.resultado = "Vitória!"
                self.__final_partida = "0"
                return
            self.atirar_teste()

        else:
            self.__jogada = "0"

    def add_embarcacoes_teste(self):
        dicionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        tamanho_oceano = self.__partida.oceano_jogador.tamanho_oceano
        contador = 0
        while True:
            if contador == 8:
                return
            elif contador < 3:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 1))
                    posicao_y = random.randint(0, (tamanho_oceano - 1))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    posicao_ocupada = False
                    for posicoes in self.__partida.oceano_jogador.posicoes_barcos.values():
                        if posicao1 == posicoes:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicao1)
                        contador += 1
                        break
            elif contador < 5:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 2))
                    posicao_y = random.randint(0, (tamanho_oceano - 2))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                    posicoes = [posicao1, posicao2]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                        contador += 1
                        break
            elif contador < 7:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 3))
                    posicao_y = random.randint(0, (tamanho_oceano - 3))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                        posicao3 = dicionario[posicao_x] + str(posicao_y + 2)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                        posicao3 = dicionario[posicao_x + 2] + str(posicao_y)
                    posicoes = [posicao1, posicao2, posicao3]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                        contador += 1
                        break
            else:
                while True:
                    posicao_x = random.randint(0, (tamanho_oceano - 4))
                    posicao_y = random.randint(0, (tamanho_oceano - 4))
                    posicao1 = dicionario[posicao_x] + str(posicao_y)
                    horizontal_ou_vertical = random.randint(0, 1)
                    if horizontal_ou_vertical == 1:
                        posicao2 = dicionario[posicao_x] + str(posicao_y + 1)
                        posicao3 = dicionario[posicao_x] + str(posicao_y + 2)
                        posicao4 = dicionario[posicao_x] + str(posicao_y + 3)
                    else:
                        posicao2 = dicionario[posicao_x + 1] + str(posicao_y)
                        posicao3 = dicionario[posicao_x + 2] + str(posicao_y)
                        posicao4 = dicionario[posicao_x + 3] + str(posicao_y)
                    posicoes = [posicao1, posicao2, posicao3, posicao4]
                    posicao_ocupada = False
                    for posicoes2 in self.__partida.oceano_jogador.posicoes_barcos.values():
                        if posicao1 in posicoes2 or posicao2 in posicoes2 or posicao3 in posicoes2 or posicao4 in \
                                posicoes2:
                            posicao_ocupada = True
                    if not posicao_ocupada:
                        self.__partida.add_barco_oceano(self.__partida.embarcacoes_jogador[contador], posicoes)
                        contador += 1
                        break
