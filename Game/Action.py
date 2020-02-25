from abc import ABC
class Action(ABC):
    def __init__(self,id):
        self.__id = id
    def getId(self):
        return self.__id
    def run(self):
        pass