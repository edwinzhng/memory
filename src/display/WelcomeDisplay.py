import sys

from colorama import Fore, Style

from blessed import Terminal
from src.util.enums import Difficulties, Modes

memory_ascii = '''
  ___  ___                                
  |  \/  |                                
  | .  . | ___ _ __ ___   ___  _ __ _   _ 
  | |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | |
  | |  | |  __/ | | | | | (_) | |  | |_| |
  \_|  |_/\___|_| |_| |_|\___/|_|   \__, |
                                    __/ /
                                   |___/
'''

class WelcomeDisplay:
  def __init__(self):
    self.term = Terminal()

  def display(self):
    mode = 0
    difficulty = 0
    self.print_welcome(mode, difficulty, 0)

    with self.term.cbreak():
      key = None
      while not key or key.name is not 'KEY_ENTER':
          key = self.term.inkey()
          mode = self.select_mode(key, mode)
          self.print_welcome(mode, difficulty, 0)

      if mode is 0:
        return Modes.SOLO, None

      key = None
      self.print_welcome(mode, difficulty, 1)

      while not key or key.name is not 'KEY_ENTER':
          key = self.term.inkey()
          difficulty = self.select_difficulty(key, mode)
          self.print_welcome(mode, difficulty, 1)

      return Modes.CPU, Difficulties.NORMAL if difficulty is 0 else Difficulties.HARD
      
  def select_mode(self, key, mode) -> str:
    if key.name is 'KEY_UP':
      return 0
    elif key.name is 'KEY_DOWN':
      return 1
    return mode

  def select_difficulty(self, key, difficulty) -> int:
    if key.name is 'KEY_UP':
      return 0
    elif key.name is 'KEY_DOWN':
      return 1
    return difficulty

  def print_welcome(self, mode, difficulty, step):
    self.term.clear()
    with self.term.fullscreen():
      print(Fore.CYAN + memory_ascii + Fore.RESET + '\n')

      print('  Select a game mode\n')
      mode_color = Fore.CYAN if step is 0 else Fore.GREEN
      self.print_selection(Modes, mode, mode_color)

      if step is 1:
        print('\n  Select difficulty\n')
        self.print_selection(Difficulties, difficulty, Fore.CYAN)

  def print_selection(self, options, selected, color):
    options = [e.value for e in options]
    for i in range(len(options)):
      if i is selected:
        print('  ' + color + options[i] + '*' + Fore.RESET)
      else:
        print('  ' + options[i])
