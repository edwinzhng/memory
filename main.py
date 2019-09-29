from src.CPUGame import CPUGame
from src.display.WelcomeDisplay import WelcomeDisplay
from src.SoloGame import SoloGame
from src.util.enums import Difficulties, Modes

if __name__ == "__main__":
  welcome_display = WelcomeDisplay()
  mode, difficulty = welcome_display.display()

  game = None
  if mode is Modes.SOLO:
    game = SoloGame()
  else:
    game = CPUGame(difficulty)
  
  game.start_game()
