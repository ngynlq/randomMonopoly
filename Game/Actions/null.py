from Game.Interface.Action import Action

class Null(Action):
    def __init__(self):
        super().__init__(id=None)
    def run():
        pass