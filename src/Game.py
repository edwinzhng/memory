from src.Card import Card
from src.util.enums import CardValue, Suit


class Game:
  def __init__(self):
    self.cards = [Card(value, suit) for value in CardValue for suit in Suit]
    self.matched_pairs = []
    self.score = 0
    self.high_score = 0
