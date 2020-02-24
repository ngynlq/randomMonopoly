from Game.Player import Player
class Game():
    def __init__(self,players=[]):
        self.__gameOver = False
        self.__players = players
    def getGameOver(self):
        return self.__gameOver
    def setPlayers(self,val):
        self.__players = val
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

if __name__ == "__main__":
    pass