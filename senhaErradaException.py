class SenhaErradaException(Exception):
    def __init__(self):
        super().__init__("Senha Errada")