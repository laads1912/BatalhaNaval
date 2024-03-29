from entidade.jogador import Jogador
from limite.tela_jogador import TelaJogador
from entidade.partida import Partida
from entidade.jogador_dao import JogadorDAO
from senhaErradaException import SenhaErradaException


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
        self.__jogador_DAO = JogadorDAO()

    def pega_jogador_pelo_nome(self, nome: str):
        jogadores = self.__jogador_DAO.get_all()
        for jogador_temp in jogadores:
            if jogador_temp.nome == nome:
                return jogador_temp
        return None

    def add_jogador(self):
        jogadores = self.__jogador_DAO.get_all()
        while True:
            dados = self.__tela_jogador.pegar_dados_jogador()
            if dados is None:
                return
            for jogador_temp in jogadores:
                if jogador_temp.nome == dados["nome"]:
                    self.__tela_jogador.mostrar_mensagem("Jogador já cadastrado.")
                    return
            jogador_temp = Jogador(dados["nome"], dados["senha"], dados["data_nascimento"])
            if dados["nome"] != "" and dados["senha"] != "" and dados["data_nascimento"]:
                self.__jogador_DAO.add(jogador_temp)
                return
            else:
                self.__tela_jogador.mostrar_mensagem("Por favor preencha todos os campos.")
                return

    def listar_jogadores(self):
        self.__tela_jogador.mostrar_mensagem("----- LISTA DE JOGADORES -----")
        jogadores = self.__jogador_DAO.get_all()
        if jogadores is None:
            self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado.")
            return
        for jogador_temp in jogadores:
            dados_jogador = {"nome": jogador_temp.nome, "data_nascimento": jogador_temp.data_nascimento}
            self.__tela_jogador.mostrar_jogador(dados_jogador)

    def mostrar_ranking(self):
        jogadores = self.__jogador_DAO.get_all()
        jogadores_temp = list(jogadores)
        if jogadores is None:
            self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado.")
        elif len(jogadores) == 0:
            self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado.")
        else:
            ranking = []
            while len(jogadores_temp) != 0:
                maior_pontuacao = 0
                melhor_jogador = None
                for jogador_temp in jogadores_temp:
                    if jogador_temp.pontuacao >= maior_pontuacao:
                        melhor_jogador = jogador_temp
                        maior_pontuacao = jogador_temp.pontuacao
                ranking.append(melhor_jogador)
                jogadores_temp.remove(melhor_jogador)

            contador = len(jogadores)
            self.__tela_jogador.mostrar_mensagem("----- RANKING -----")
            for jogador_temp in ranking[::-1]:
                self.__tela_jogador.mostrar_mensagem(f'{contador} - {jogador_temp.nome} -> Pontuação: {jogador_temp.pontuacao}')
                contador -= 1

    def del_jogador(self):
        while True:
            self.listar_jogadores()
            dados = self.__tela_jogador.selecionar_jogador()
            if dados is None:
                return
            jogador_temp = self.__jogador_DAO.get(dados["nome"])
            if jogador_temp is not None:
                try:
                    if jogador_temp.senha == dados["senha"]:
                        self.__jogador_DAO.remove(jogador_temp.nome)
                        self.listar_jogadores()
                        return
                    else:
                        raise SenhaErradaException
                except SenhaErradaException:
                    self.__tela_jogador.mostrar_mensagem("Senha Inválida")
                    return
            else:
                self.__tela_jogador.mostrar_mensagem("Jogador não encontrado")
                return

    def alterar_cadastro(self):
        jogadores = self.__jogador_DAO.get_all()
        while True:
            if jogadores is None:
                self.__tela_jogador.mostrar_mensagem("Nenhum jogador cadastrado")
                return
            elif len(jogadores) != 0:
                self.listar_jogadores()
                dados = self.__tela_jogador.selecionar_jogador()
                if dados is None:
                    return
                jogador_temp = self.__jogador_DAO.get(dados["nome"])
                if jogador_temp is not None:
                    try:
                        if jogador_temp.senha == dados["senha"]:
                            lista_opcoes = {"nome": 1, "senha": 2, "data_nascimento": 3, "retornar": 0}
                            opcao = self.__tela_jogador.opcoes_alterar_cadastro()
                            if opcao is None:
                                return
                            if opcao == "":
                                self.__tela_jogador.mostrar_mensagem("Opção inválida")
                                return
                            elif opcao == 'Nome':
                                novo_nome = self.__tela_jogador.alterar_nome()
                                self.__jogador_DAO.update(jogador_temp.nome, 'nome', novo_nome)
                                jogador_temp.nome = novo_nome
                                self.__tela_jogador.mostrar_mensagem("Nome alterado com sucesso!")
                                return
                            elif opcao == 'Senha':
                                nova_senha = self.__tela_jogador.alterar_senha()
                                self.__jogador_DAO.update(jogador_temp.senha, 'senha', nova_senha)
                                jogador_temp.senha = nova_senha
                                self.__tela_jogador.mostrar_mensagem("Senha alterada com sucesso!")
                                return
                            elif opcao == 'Data de nascimento':
                                nova_data = self.__tela_jogador.alterar_data_nascimento()
                                self.__jogador_DAO.update(jogador_temp.data_nascimento, 'data_nascimento', nova_data)
                                jogador_temp.data_nascimento = nova_data
                                self.__tela_jogador.mostrar_mensagem("Data de nascimento alterada com sucesso!")
                                return
                            else:
                                self.__tela_jogador.mostrar_mensagem("Opção inválida")
                                return
                        else:
                            raise SenhaErradaException
                    except SenhaErradaException:
                        self.__tela_jogador.mostrar_mensagem("Senha Errada")
                    try:
                        if jogador_temp.senha == dados["senha"]:
                            lista_opcoes = {"nome": 1, "senha": 2, "data_nascimento": 3, "retornar": 0}
                            opcao = self.__tela_jogador.opcoes_alterar_cadastro()
                            if opcao is None:
                                return
                            if opcao == "":
                                self.__tela_jogador.mostrar_mensagem("Opção inválida")
                                return
                            elif opcao == 'Nome':
                                novo_nome = self.__tela_jogador.alterar_nome()
                                self.__jogador_DAO.update(jogador_temp.nome, 'nome', novo_nome)
                                jogador_temp.nome = novo_nome
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
                            raise SenhaErradaException
                    except SenhaErradaException:
                        self.__tela_jogador.mostrar_mensagem("Senha Inválida")
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
            jogador_temp = self.__jogador_DAO.get(dados["nome"])
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

    def add_partida(self, nome, partida):
        self.__jogador_DAO.update(nome, 'partida', partida)

    def add_pontuacao(self, nome, ponto):
        self.__jogador_DAO.update(nome, 'pontuacao', ponto)
