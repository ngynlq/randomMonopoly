class Player():
    def __init__(self,money=0,name=""):
        self._pos = 0
        self._alive = True
        self._money = money
        self._skip = False
        self._name = name
    def setPos(self,pos):
        self._pos = pos
    def getPos(self):
        return self._pos;
    def rollDie(self,dice1,dice2):
        self._pos = dice1,dice2
    def updateMoney(self,val):
        self._money +=val
    def setMoney(self,val):
        self._money = val;
    def getAlive(self):
        return self._alive
    def getMoney(self):
        return self._money;
    def skipTurn(self):
        self._skip = True
    def getActiveTurn(self):
        return self._skip
    def setAlive(self,val):
        self._alive = val