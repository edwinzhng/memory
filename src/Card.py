from src.util.enums import CardValue, Suit

class Card:
  def __init__(self, value: CardValue, suit: Suit):
    self.value: CardValue = value
    self.suit: Suit = suit

  def value(self) -> CardValue:
    return self.value

  def suit(self) -> Suit:
    return self.suit