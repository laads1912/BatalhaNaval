from entidade.partida import Partida


class Jogador:
    def __init__(self, nome: str, senha: str, data_nascimento: str):
        self.__nome = nome
        self.__senha = senha
        self.__data_nascimento = data_nascimento
        self.__partidas = []
        self.__pontuacao = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def partidas(self):
        return self.__partidas

    @property
    def pontuacao(self):
        return self.__pontuacao

    def add_partida(self, partida: Partida):
        self.__partidas.append(partida)

    def del_partida(self, partida: Partida):
        self.__partidas.pop(self.__partidas.index(partida))

    def add_pontuacao(self, ponto):
        self.__pontuacao += ponto
