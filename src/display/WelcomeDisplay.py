from colorama import Fore

from src.display.Display import Display
from src.util.enums import Difficulty


class WelcomeDisplay(Display):
  def display(self):
    with self.term.fullscreen():
      difficulty = 0
      self.print_header()
      self.print_difficulty(difficulty, Fore.LIGHTCYAN_EX)

      with self.term.cbreak():
        key = None
        while not key or key.name != 'KEY_ENTER':
          key = self.term.inkey()
          difficulty = self.select_difficulty(key, difficulty)
          self.print_difficulty(difficulty, Fore.LIGHTCYAN_EX)

        return Difficulty.NORMAL if difficulty == 0 else Difficulty.HARD

  def select_difficulty(self, key, difficulty) -> int:
    if key.name == 'KEY_UP':
      return 0
    elif key.name == 'KEY_DOWN':
      return 1
    return difficulty

  def print_difficulty(self, selected, color):
    print(self.term.move(*self.refresh_location))
    print('  Navigate using UP ↑ and DOWN ↓\n')
    print(Fore.LIGHTMAGENTA_EX + '  Press ENTER to select difficulty\n' + Fore.WHITE)
    options = [e.value for e in Difficulty]
    for i in range(len(options)):
      if i == selected:
        print('  ' + color + options[i] + '*' + Fore.WHITE)
      else:
        print('  ' + options[i] + ' ')
    print()

    if selected == 0:
      print(Fore.LIGHTGREEN_EX + "\n  Normal Difficulty:" + Fore.WHITE)
      print("  Matching pairs count as 1 point ")
      print("  You lose 1 point if you fail to match a card that was already seen ")
      print("                                                                     ")
    else:
      print(Fore.LIGHTGREEN_EX + "\n  Hard Difficulty:  " + Fore.WHITE)
      print("  Matching pairs count as 3 points")
      print("  You lose 1 point any time you fail to find a match                 ")
      print("  You lose 2 points if you fail to match a card that was already seen")
