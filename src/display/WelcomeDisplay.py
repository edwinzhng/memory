from colorama import Fore

from src.util.enums import Difficulty
from src.util.constants import MEMORY_ASCII


class WelcomeDisplay:
  def __init__(self, terminal):
    self.term = terminal
    self.term.clear()

  def get_input(self):
    difficulty = 0
    self.print_welcome(difficulty)

    with self.term.cbreak():
      key = None
      while not key or key.name is not 'KEY_ENTER':
          key = self.term.inkey()
          difficulty = self.select_difficulty(key, difficulty)
          self.print_welcome(difficulty)

      return Difficulty.NORMAL if difficulty is 0 else Difficulty.HARD
      
  def select_difficulty(self, key, difficulty) -> int:
    if key.name is 'KEY_UP':
      return 0
    elif key.name is 'KEY_DOWN':
      return 1
    return difficulty

  def print_welcome(self, difficulty):
    self.term.clear()
    with self.term.fullscreen():
      print(Fore.LIGHTCYAN_EX + MEMORY_ASCII + Fore.RESET)
      print(Fore.LIGHTRED_EX + '__________' + Fore.LIGHTYELLOW_EX + '__________' + \
            Fore.LIGHTGREEN_EX + '__________' + Fore.LIGHTCYAN_EX + '__________' + \
            Fore.LIGHTBLUE_EX + '__________' + Fore.LIGHTMAGENTA_EX + '__________' + \
            '\n\n' + Fore.RESET)
      print(Fore.LIGHTMAGENTA_EX + '\n  Press ENTER to select difficulty\n' + Fore.RESET)
      self.print_selection(Difficulty, difficulty, Fore.LIGHTCYAN_EX)

  def print_selection(self, options, selected, color):
    options = [e.value for e in options]
    for i in range(len(options)):
      if i is selected:
        print('  ' + color + options[i] + '*' + Fore.RESET)
      else:
        print('  ' + options[i])
