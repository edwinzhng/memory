import random
from abc import ABC, abstractmethod

from src.Card import Card
from src.util.enums import CardValue, Suit

NUM_PAIRS = 12
CARDS_PER_ROW = 6

class Game(ABC):
  def __init__(self):
    self.all_cards = [Card(value, suit) for value in CardValue for suit in Suit]
    super().__init__()

  @abstractmethod
  def reset(self) -> None:
    self.reset_board()

  @abstractmethod
  def move(self, first_card: (int, int), second_card: (int, int)) -> int:
    pass

  def reset_board(self) -> None:
    cards = random.sample(self.all_cards, NUM_PAIRS) * 2
    random.shuffle(cards)
    self.board = [cards[i:i+CARDS_PER_ROW] for i in range(0, NUM_PAIRS * 2, CARDS_PER_ROW)]
    self.player_pairs = []

  def start_game(self) -> None:
    self.reset()
