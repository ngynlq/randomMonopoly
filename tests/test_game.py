from Game.Game import Game
from Game.Player import Player
from Game.Interface.Action import Action
from Game.Actions import *

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
    game.setPlayers([Player()])
    game.move(0,6,6)
    assert game.getPlayer(0).getPos() == 12

def test_roll_wrap():
    game = Game()
    game.setPlayers([Player()])
    game.move(0,40,6)
    assert game.getPlayer(0).getPos() == 6

def test_payAll_one():
    game = Game()
    game.setPlayers([Player(),Player()])
    game.payAll(0,50)
    assert game.getPlayer(0).getMoney() == -50
    assert game.getPlayer(1).getMoney() == 50

def test_payAll_two():
    game = Game()
    game.setPlayers([Player(),Player(),Player()])
    game.payAll(0,50)
    assert game.getPlayer(0).getMoney() == -100
    assert game.getPlayer(1).getMoney() == 50
    assert game.getPlayer(2).getMoney() == 50

def test_collect_all():
    game = Game()
    game.setPlayers([Player(),Player(),Player()])
    game.collectAll(0,50)
    assert game.getPlayer(0).getMoney() == 100
    assert game.getPlayer(1).getMoney() == -50
    assert game.getPlayer(2).getMoney() == -50

def test_payPool():
    game = Game()
    game.addToPool(500)
    assert game.getPool() == 500
    game.addToPool(55)
    assert game.getPool() == 555

def test_moveToJail():
    game = Game(players=[Player()])
    game.setBoard([null.Null(),jail.Jail()])
    game.moveToJail(0)
    assert game.getPlayer(0).getJail() == True
    assert game.getPlayer(0).getPos() == 1







