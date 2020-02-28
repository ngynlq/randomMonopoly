from Game.Player import Player
from Game.Game import Game
from Game.Actions.jail import Jail
def test_jail():
    sq = Jail()
    assert sq.getId() == 'jail'

def test_just_visiting():
    """"
    Handles test case of landing on the jail/just visting
    """

    sq = Jail()
    p = Player()
    game = Game(players=[p])
    old = game.getPlayers()
    sq.run(0,game)
    ran = game.getPlayers()
    #current player and all players
    assert old == ran