from src.util.enums import CardValue, Suit
from colorama import Fore

class Card:
  def __init__(self, value: CardValue, suit: Suit):
    self.value: CardValue = value
    self.suit: Suit = suit
    self.color = Fore.LIGHTCYAN_EX if suit in [Suit.SPADES, Suit.CLUBS] else Fore.LIGHTRED_EX

  def __str__(self):
    return self.color + '{}{}'.format(self.value.value, self.suit.value) + Fore.WHITE

  def __repr__(self):
    return self.color + '{}{}'.format(self.value.value, self.suit.value) + Fore.WHITE

  def __eq__(self, other):
      if isinstance(other, Card):
          return self.value == other.value and self.suit == other.suit
      return False

  def __hash__(self):
    return hash('{} of {}'.format(self.value.name, self.suit.name))

  # displays card with proper colors and formatting in the terminal
  def display(self, terminal, cursor_start, flipped=False, selected=False):
    color = Fore.WHITE if not selected else Fore.LIGHTMAGENTA_EX
    if flipped:
      color = self.color

    x, y = cursor_start
    print(terminal.move(x, y) + color + ' _____ ')
    if flipped:
      content = '    ' if len(self.value.value) == 1 else '   '
      print(terminal.move(x + 1, y) + '|{}{}|'.format(self.value.value, content))
      print(terminal.move(x + 2, y) + '|{0} {0} {0}|'.format(self.suit.value))
      content = '____' if len(self.value.value) == 1 else '___'
      print(terminal.move(x + 3, y) + '|{}{}|'.format(content, self.value.value) + Fore.WHITE)
    else:
      print(terminal.move(x + 1, y) + '|     |')
      print(terminal.move(x + 2, y) + '|KPCB |')
      print(terminal.move(x + 3, y) + '|_____|' + Fore.WHITE)
