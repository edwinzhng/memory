from enum import Enum

class Suit(Enum):
  CLUBS = 1
  DIAMONDS = 2
  HEARTS = 3
  SPADES = 4

class CardValue(Enum):
  ACE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13