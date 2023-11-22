from entidade.jogador import Jogador
from limite.tela_jogador import TelaJogador
from entidade.partida import Partida


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema

    def pega_jogador_pelo_nome(self, nome: str):
        for jogador_temp in self.__jogadores:
            if jogador_temp.nome == nome:
                return jogador_temp
        return None

    def add_jogador(self):
        while True:
            dados = self.__tela_jogador.pegar_dados_jogador()
            if dados is None:
                return
            jogador_temp = Jogador(dados["nome"], dados["senha"], dados["data_nascimento"])
            if dados["nome"] != "" and dados["senha"] != "" and dados["data_nascimento"]:
                self.__jogadores.append(jogador_temp)
                return
            else:
                self.__tela_jogador.mostrar_mensagem("Por favor preencha todos os campos.")
                return

    def listar_jogadores(self):
        self.__tela_jogador.mostrar_mensagem("----- LISTA DE JOGADORES -----")
        for jogador_temp in self.__jogadores:
            dados_jogador = {"nome": jogador_temp.nome, "data_nascimento": jogador_temp.data_nascimento}
            self.__tela_jogador.mostrar_jogador(dados_jogador)

    def mostrar_ranking(self):
        if len(self.__jogadores) == 0:
            self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado.")
        else:
            jogadores_temp = self.__jogadores[:]
            ranking = []
            while len(jogadores_temp) != 0:
                maior_pontuacao = 0
                melhor_jogador = 0
                for j in jogadores_temp:
                    if j.pontuacao >= maior_pontuacao:
                        melhor_jogador = j
                ranking.append(melhor_jogador)
                jogadores_temp.remove(melhor_jogador)

            contador = len(self.__jogadores)
            self.__tela_jogador.mostrar_mensagem("----- RANKING -----")
            for jogador_temp in ranking:
                self.__tela_jogador.mostrar_mensagem(f'{contador} - {jogador_temp.nome} -> Pontuação: {jogador_temp.pontuacao}')
                contador -= 1

    def del_jogador(self):
        while True:
            self.listar_jogadores()
            dados = self.__tela_jogador.selecionar_jogador()
            if dados is None:
                return
            jogador_temp = self.pega_jogador_pelo_nome(dados["nome"])
            if jogador_temp is not None:
                if jogador_temp.senha == dados["senha"]:
                    self.__jogadores.remove(jogador_temp)
                    self.listar_jogadores()
                    return
                else:
                    self.__tela_jogador.mostrar_mensagem("Senha inválida.")
                    return
            else:
                self.__tela_jogador.mostrar_mensagem("Jogador não encontrado")
                return

    def alterar_cadastro(self):
        while True:
            if len(self.__jogadores) != 0:
                self.listar_jogadores()
                dados = self.__tela_jogador.selecionar_jogador()
                if dados is None:
                    return
                jogador_temp = self.pega_jogador_pelo_nome(dados["nome"])
                if jogador_temp is not None:
                    if jogador_temp.senha == dados["senha"]:
                        lista_opcoes = {"nome": 1, "senha": 2, "data_nascimento": 3, "retornar": 0}
                        opcao = self.__tela_jogador.opcoes_alterar_cadastro()
                        if opcao is None:
                            return
                        if opcao == "":
                            self.__tela_jogador.mostrar_mensagem("Opção inválida")
                            return
                        elif opcao == 'Nome':
                            jogador_temp.nome = self.__tela_jogador.alterar_nome()
                            self.__tela_jogador.mostrar_mensagem("Nome alterado com sucesso!")
                            return
                        elif opcao == 'Senha':
                            jogador_temp.senha = self.__tela_jogador.alterar_senha()
                            self.__tela_jogador.mostrar_mensagem("Senha alterada com sucesso!")
                            return
                        elif opcao == 'Data de nascimento':
                            jogador_temp.data_nascimento = self.__tela_jogador.alterar_data_nascimento()
                            self.__tela_jogador.mostrar_mensagem("Data de nascimento alterada com sucesso!")
                            return
                        else:
                            self.__tela_jogador.mostrar_mensagem("Opção inválida")
                            return
                    else:
                        self.__tela_jogador.mostrar_mensagem("Senha inválida.")
                        return
                else:
                    self.__tela_jogador.mostrar_mensagem("Jogador não encontrado")
                    return
            else:
                self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado")
                return

    def mostrar_historico(self):
        while True:
            self.listar_jogadores()
            dados = self.__tela_jogador.selecionar_jogador()
            if dados is None:
                return
            jogador_temp = self.pega_jogador_pelo_nome(dados["nome"])
            contador = 1
            if jogador_temp is not None:
                for partida in jogador_temp.partidas:
                    jogadas = " ".join(partida.oceano_jogador.tiros_realizados)
                    self.__tela_jogador.mostrar_partida(partida, jogadas, contador)
                    contador += 1
                return
            else:
                self.__tela_jogador.mostrar_mensagem("Jogador não encontrado")
                return

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_jogador, 2: self.mostrar_ranking, 3: self.del_jogador, 4: self.alterar_cadastro,
                        5: self.mostrar_historico, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_jogador.tela_opcoes()
            if opcao_escolhida == "":
                self.__tela_jogador.mostrar_mensagem("Opção inválida")
            elif opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_jogador.mostrar_mensagem("Opção inválida")
