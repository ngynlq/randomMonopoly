from Game.Actions.FreeParking import FreeParking
from Game.Player import Player
from Game.Game import Game

def test_collectPool():
    game = Game(players=[Player()])
    sq = FreeParking()
    game.setPool(100)
    assert game.getPool() == 100
    sq.run(0,game)
    assert game.getPool() == 0
    assert game.getPlayer(0).getMoney() == 100
