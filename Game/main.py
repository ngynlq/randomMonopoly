from Game.Game import Game
from Game.TurnOrder import TurnOrder
from Game.rules import Rules
if __name__ == "__main__":
    game = Game()
    turn = TurnOrder(range(len(game.getPlayers())))
    order = iter(turn)
    manager = Rules(game)
    while(not game.getGameOver()):
        currentPlayer = game.getPlayer(next(order))
        roll1 = random()
        roll2 = random()
        manager.roll(currentPlayer,roll1,roll2)
        manager.landSquare()
        #game.action(handleInput())
        #trade . upgrade . end
        #accept end turn or other actions
        #GUI.update(game)
        game.checkGameOver()