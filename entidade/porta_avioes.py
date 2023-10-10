from entidade.embarcacao import Embarcacao


class PortaAvioes(Embarcacao):

    def __init__(self, vida):
        super().__init__(vida)

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, num):
        self.__vida = num
