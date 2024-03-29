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

    def update(self, key: str, attribute_name: str, new_value):
        if isinstance(key, str) and isinstance(attribute_name, str):
            super().update(key, attribute_name, new_value)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
