class Rules():
    #likely sub-interface of phases
    def __init__(self,game,jail=3):
        self.__game = game
        self.__roll = False
        self.__jail = jail
    def roll(self,player,roll1,roll2):
        play = self.__game.getPlayer(player)   
        if self.__game.checkDouble(play,roll1,roll2):
            self.__roll = True
            play.incrementDouble()
        if play.getDouble() == self.__jail:
            self.__game.moveToJail(player)
        else:
            self.__game.move(player,roll1,roll2)
    def landSquare(self,index):
        self.__game.runAction(index)

    def getRollAgain(self):
        return self.__roll