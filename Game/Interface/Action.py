from abc import ABC
from abc import abstractmethod
class Action(ABC):
    def __init__(self,id):
        self.__id = id
    def getId(self):
        return self.__id
    @abstractmethod
    def run(self):
        pass