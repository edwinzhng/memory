from blessed import Terminal
from src.display.WelcomeDisplay import WelcomeDisplay
from src.Game import Game

if __name__ == "__main__":
  terminal = Terminal()
  welcome_display = WelcomeDisplay(terminal)
  difficulty = welcome_display.get_input()

  game = Game(terminal, difficulty)
  game.run()
