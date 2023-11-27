class PosicaoInvalidaEception(Exception):
    def __init__(self):
        super().__init__("Posição Inválida")
