from Game.Game import Game
if __name__ == "__main__":
    game = Game()
    while(not game.getGameOver()):
        currentPlayer = game.getPlayer()
        game.roll()
        game.checkGameOver()