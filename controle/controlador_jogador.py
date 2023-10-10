from entidade.jogador import Jogador
from limite.tela_jogador import TelaJogador
from entidade.partida import Partida


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema

    def pega_jogador_pelo_nome(self, nome: str):
        for jogador in self.__jogadores:
            if jogador.nome() == nome:
                return jogador
        return None

    def add_jogador(self):
        dados = self.__tela_jogador.pegar_dados_jogador()
        jogador = Jogador(dados["nome"], dados["data_nascimento"])
        self.__jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.__jogadores:
            self.__tela_jogador.mostrar_jogador({"nome": jogador.nome(), "data_nascimento": jogador.data_nascimento()})

    def mostrar_ranking(self):
        jogadores = self.__jogadores
        ranking = []
        while len(jogadores) != 0:
            maior_pontuacao = 0
            melhor_jogador = 0
            for j in jogadores:
                if j.pontuacao() >= maior_pontuacao:
                    melhor_jogador = j
            ranking.append(melhor_jogador)
            jogadores.remove(melhor_jogador)

        contador = 1
        for jogador in ranking:
            print(f'{contador} - {jogador.nome()}')
            print(f'Pontuação: {jogador.pontuacao()}')
            print()
            contador += 1

    def del_jogador(self):
        self.listar_jogadores()
        nome = self.__tela_jogador.selecionar_jogador()
        jogador = self.pega_jogador_pelo_nome(nome)
        if jogador is not None:
            self.__jogadores.remove(jogador)
            self.listar_jogadores()
        else:
            self.__tela_jogador.mostrar_mensagem("Jogador não existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_jogador(), 2: self.mostrar_ranking(), 3: self.del_jogador(), 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()
