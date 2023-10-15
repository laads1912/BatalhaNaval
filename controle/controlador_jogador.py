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
        dados = self.__tela_jogador.pegar_dados_jogador()
        jogador_temp = Jogador(dados["nome"], dados["senha"], dados["data_nascimento"])
        self.__jogadores.append(jogador_temp)

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

            contador = 1
            self.__tela_jogador.mostrar_mensagem("----- RANKING -----")
            for jogador_temp in ranking:
                self.__tela_jogador.mostrar_mensagem(f'{contador} - {jogador_temp.nome}')
                self.__tela_jogador.mostrar_mensagem(f'Pontuação: {jogador_temp.pontuacao}')
                self.__tela_jogador.mostrar_mensagem("")
                contador += 1

    def del_jogador(self):
        while True:
            self.listar_jogadores()
            dados = self.__tela_jogador.selecionar_jogador()
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
            self.listar_jogadores()
            dados = self.__tela_jogador.selecionar_jogador()
            jogador_temp = self.pega_jogador_pelo_nome(dados["nome"])
            if jogador_temp is not None:
                if jogador_temp.senha == dados["senha"]:
                    lista_opcoes = {"nome": 1, "senha": 2, "data_nascimento": 3, "retornar": 0}
                    opcao = self.__tela_jogador.opcoes_alterar_cadastro()
                    if opcao == lista_opcoes["nome"]:
                        jogador_temp.nome = self.__tela_jogador.alterar_nome()
                        self.__tela_jogador.mostrar_mensagem("Nome alterado com sucesso!")
                        return
                    elif opcao == lista_opcoes["senha"]:
                        jogador_temp.senha = self.__tela_jogador.alterar_senha()
                        self.__tela_jogador.mostrar_mensagem("Senha alterada com sucesso!")
                        return
                    elif opcao == lista_opcoes["data_nascimento"]:
                        jogador_temp.data_nascimento = self.__tela_jogador.alterar_data_nascimento()
                        self.__tela_jogador.mostrar_mensagem("Data de nascimento alterada com sucesso!")
                        return
                    else:
                        return
                else:
                    self.__tela_jogador.mostrar_mensagem("Senha inválida.")
                    return
            else:
                self.__tela_jogador.mostrar_mensagem("Jogador não encontrado")
                return

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_jogador, 2: self.mostrar_ranking, 3: self.del_jogador, 4: self.alterar_cadastro,
                        0: self.retornar}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_jogador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

