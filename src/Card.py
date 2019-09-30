from src.util.enums import CardValue, Suit
from colorama import Fore

class Card:
  def __init__(self, value: CardValue, suit: Suit):
    self.value: CardValue = value
    self.suit: Suit = suit
    self.color = Fore.LIGHTBLUE_EX if suit in [Suit.SPADES, Suit.CLUBS] else Fore.LIGHTRED_EX

  def __str__(self):
    return self.color + '{}{}'.format(self.value.value, self.suit.value) + Fore.RESET

  def __repr__(self):
    return self.color + '{}{}'.format(self.value.value, self.suit.value) + Fore.RESET

  def display(self, terminal, cursor_start, flipped=False, selected=False):
    color = Fore.WHITE

    if flipped:
      color = self.color
    elif selected:
      color = Fore.LIGHTCYAN_EX

    x, y = cursor_start
    print(terminal.move(x, y) + color + ' _____ ')

    if flipped:
      if len(self.value.value) is 1:
        print(terminal.move(x + 1, y) + '|{}    |'.format(self.value.value))
      else:
        print(terminal.move(x + 1, y) + '|{}   |'.format(self.value.value))

      print(terminal.move(x + 2, y) + \
            '|{} {} {}|'.format(self.suit.value, self.suit.value, self.suit.value))
  
      if len(self.value.value) is 1:
        print(terminal.move(x + 3, y) + '|____{}|'.format(self.value.value) + Fore.RESET)
      else:
        print(terminal.move(x + 3, y) + '|___{}|'.format(self.value.value) + Fore.RESET)
    else:
      print(terminal.move(x + 1, y) + '|     |')
      print(terminal.move(x + 2, y) + '|     |')
      print(terminal.move(x + 3, y) + '|_____|' + Fore.RESET)
