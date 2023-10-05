from entidade.embarcacao import Embarcacao


class Submarino(Embarcacao):

    def __init__(self, vida):
        super().__init__(vida)