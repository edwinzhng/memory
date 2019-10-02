from abc import ABC, abstractmethod

from colorama import Fore

from src.util.constants import MEMORY_ASCII


# abstract Display class for printing the game header and initialization
class Display(ABC):
  def __init__(self, terminal):
    self.term = terminal
    self.print_header()

  @abstractmethod
  def display(self):
    pass

  def print_header(self):
    print(Fore.LIGHTCYAN_EX + MEMORY_ASCII + Fore.RESET)
    print(Fore.LIGHTRED_EX + '  __________' + Fore.LIGHTYELLOW_EX + '__________' + \
          Fore.LIGHTGREEN_EX + '__________' + Fore.LIGHTCYAN_EX + '__________' + \
          Fore.LIGHTBLUE_EX + '__________' + Fore.LIGHTMAGENTA_EX + '__________' + \
          '\n' + Fore.RESET)
    self.refresh_location = self.term.get_location()
