from abc import ABC, abstractmethod

class Embarcacao(ABC):
    def __init__(self, vida: int):
        self.__vida = vida
    
    @abstractmethod
    @property
    def vida(self):
        pass

    @abstractmethod
    @vida.setter
    def vida(self, value):
        pass