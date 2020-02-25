from Game.rules import Rules
from Game.Game import Game
from Game.Player import Player
from Game.Action import Action

def test_roll():
    game = Game(players=[Player()])
    rule = Rules(game)
    rule.roll(0,6,6)
    assert game.getPlayer(0).getPos() == 12
    assert game.getPlayer(0).getDouble() == 1

def test_rollAgain():
    game = Game(players=[Player()])
    rule = Rules(game)
    rule.roll(0,6,6)
    assert rule.getRollAgain() == True

def test_rollJail_three():
    game = Game(players=[Player()])
    game.setBoard([Action(id="None"),Action(id="jail")])
    rule = Rules(game,jail=3)
    rule.roll(0,6,6)
    rule.roll(0,6,6)
    rule.roll(0,6,6)
    assert game.getPlayer(0).getDouble() == 3
    assert game.getPlayer(0).getJail() == True
    assert game.getPlayer(0).getPos() == 1
    #move to nearest jail



