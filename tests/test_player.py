from Game.Player import Player
def test_movePlayer_start():
    player = Player()
    player.setPos(0);
    assert player.getPos() == 0

def test_movePlayer_any():
    player = Player()
    player.setPos(5);
    assert player.getPos() == 5


def test_player_alive():
    player = Player()
    assert player.getAlive() == True

def test_update_money():
    player = Player()
    player.updateMoney(500)
    assert player.getMoney() == 500
def test_custom_money():
    player = Player(money=500)
    player.updateMoney(1000)
    assert player.getMoney() == 1500

def test_skip_turn():
    player = Player()
    player.skipTurn()
    assert player.getActiveTurn() == True
