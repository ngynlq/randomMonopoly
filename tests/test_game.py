from Game.Game import Game
from Game.Player import Player
def test_game_over():
    game = Game()
    assert game.getGameOver() == False

#catch typos
def test_setPlayers():
    game = Game()
    a = [Player(),Player()]
    game.setPlayers(a)
    assert game.getPlayers() != None


def test_game_over_true():
    game = Game()
    game.setPlayers([Player(),Player()])
    a = game.getPlayers()
    a[1].setAlive(False)
    game.checkGameOver()
    assert game.getGameOver() == True

def test_game_over_false_mult():
    game = Game()
    game.setPlayers([Player(),Player()])
    game.checkGameOver()
    assert game.getGameOver() == False

def test_player_alive_money():
    game = Game()
    game.setPlayers([Player()])
    player = game.getPlayers()[0]
    player.setMoney(0)
    game.checkMoneyRule(player)
    assert player.getAlive() == False

def test_roll():
    game = Game()
    game.roll()






