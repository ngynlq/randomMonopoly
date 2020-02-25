class TurnOrder():
    def __init__(self,order=[]):
        self.__order = order
        self.__pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.__order) <= 0:
            raise StopIteration
        else:
            res = self.__order[self.__pos]
            self.__boundLength()
            return res
    def __boundLength(self):
        self.__pos = (1 +self.__pos) % len(self.__order)
    def reverseOrder(self):
        self.__order = self.__order[self.__pos:] + self.__order[:self.__pos]
        self.__order = self.__order[::-1]
        self.__pos = 0

    