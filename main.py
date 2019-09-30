from blessed import Terminal
from src.display.WelcomeDisplay import WelcomeDisplay
from src.Game import Game

if __name__ == "__main__":
  terminal = Terminal()
  welcome = WelcomeDisplay(terminal)
  difficulty = welcome.display()
  game = Game(terminal, difficulty)
  game.run()
