from entidade.embarcacao import Embarcacao


class Bote(Embarcacao):

    def __init__(self, vida):
        super().__init__(vida)
        self.__nome = "bote"

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, num):
        self.__vida = num

    @property
    def nome(self):
        return self.__nome