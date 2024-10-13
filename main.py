from Game import Game
from States.AppState import AppState

g: Game = Game()
g.load_state(AppState(g))
g.game_loop()