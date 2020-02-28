from Game.Interface.Action import Action

class FreeParking(Action):
    def __init__(self):
        super().__init__(id="FreeParking")
    def run(self,index,game):
        money = game.getPool()
        game.setPool(0)
        game.getPlayer(index).updateMoney(money)
