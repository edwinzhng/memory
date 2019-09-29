from src.util.enums import CardValue, Suit

class Card:
  def __init__(self, value: CardValue, suit: Suit):
    self.value: CardValue = value
    self.suit: Suit = suit

  def __str__(self):
    return '{} of {}'.format(self.value.name, self.suit.name)

  def __repr__(self):
    return '{} of {}'.format(self.value.name, self.suit.name)
