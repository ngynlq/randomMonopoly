from Game.Player import Player
from Game.TurnOrder import TurnOrder
class Game():
    def __init__(self,players=[],board =[]):
        self.__gameOver = False
        self.__players = players
        self.__board = list(range(40))
        self.__pool = 0
        self.__chance = []
        self.__chest = []
    def setBoard(self,board):
        self.__board = board
    def getGameOver(self):
        return self.__gameOver
    def setPlayers(self,val):
        self.__players = val
    def getPlayer(self,val):
        return self.__players[val]
    def getPlayers(self):
        return self.__players
    def checkGameOver(self):
        self.__gameOver = True if self.getRemaining() <=1 else False
    def getRemaining(self):
        remaining = 0
        for i in self.__players:
            if i.getAlive():
                remaining += 1
        return remaining
    def checkMoneyRule(self,player):
        if player.getMoney() <= 0:
            player.setAlive(False)
    def move(self,index,roll1,roll2):
        player = self.__players[index]
        pos = player.getPos()
        player.setPos((pos +roll1+roll2)%len(self.__board))
    def payAll(self,index,amount):
        player = self.__players[index]
        other = self.__players[index+1:] + self.__players[:index]
        player.updateMoney(-50*len(other))
        for play in other:
            play.updateMoney(50)
    def checkDouble(self,player,roll1,roll2):
        return  roll1 == roll2
    def collectAll(self,index,amount):
        player = self.__players[index]
        other = self.__players[index+1:] + self.__players[:index]
        player.updateMoney(50*len(other))
        for play in other:
            play.updateMoney(-50)
    def addToPool(self,amount):
        self.__pool +=amount
    def getPool(self):
        return self.__pool
    def _findNearestJail(self):
        pos = 0
        for i in self.__board:
            if i.getId() == "jail":
                break
            pos +=1
        return pos
    def moveToJail(self,index):
        play = self.__players[index]
        play.setJail(True)
        pos = self._findNearestJail()
        play.setPos(pos)
    def runAction(self,index):
        play = self.__players[index]
        pos = play.getPos()
        self.__board[pos].run()
    def setPool(self,amount):
        self.__pool = amount
    def trade(self,seller,item,buyer,amount):
        sell = self.__players[seller]
        sell.updateMoney(500)
        deed = sell.removeDeed("a")
        buy = self.__players[buyer]
        buy.addDeed(deed)
        buy.updateMoney(-500)


if __name__ == "__main__":
    pass