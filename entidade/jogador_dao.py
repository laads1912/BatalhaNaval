from dao import DAO
from entidade.jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def add(self, jogador: Jogador):
        if ((isinstance(jogador.nome, str))
                and isinstance(jogador.senha, str)
                and isinstance(jogador.data_nascimento, str)
                and (jogador is not None)
                and isinstance(jogador, Jogador)):
            super().add(jogador.nome, jogador)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
