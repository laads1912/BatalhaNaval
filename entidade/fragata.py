from entidade.embarcacao import Embarcacao


class Fragata(Embarcacao):

    def __init__(self, vida):
        super().__init__(vida)