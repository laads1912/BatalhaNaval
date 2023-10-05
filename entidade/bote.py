from entidade.embarcacao import Embarcacao

class Bote(Embarcacao):

    def __init__(self, vida):
        super().__init__(vida)