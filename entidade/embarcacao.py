from abc import ABC, abstractmethod


class Embarcacao(ABC):
    def __init__(self, vida: int):
        self.__vida = vida

    @abstractmethod
    def vida(self):
        pass

    @abstractmethod
    def vida(self, value):
        pass
