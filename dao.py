import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except Exception:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def update(self, key, attribute_name, new_value):
        try:
            obj = self.__cache[key]
            if attribute_name == 'partida':
                obj.add_partida(new_value)
            elif attribute_name == 'pontuacao':
                obj.add_pontuacao(new_value)
            else:
                setattr(obj, attribute_name, new_value)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()
