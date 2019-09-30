from enum import Enum

class Suit(Enum):
  CLUBS = '♣'
  DIAMONDS = '♦'
  HEARTS = '♥'
  SPADES = '♠'

class CardValue(Enum):
  ACE = 'A'
  TWO = '2'
  THREE = '3'
  FOUR = '4'
  FIVE = '5'
  SIX = '6'
  SEVEN = '7'
  EIGHT = '8'
  NINE = '9'
  TEN = '10'
  JACK = 'J'
  QUEEN = 'Q'
  KING = 'K'

class Difficulty(Enum):
  NORMAL = 'normal'
  HARD = 'hard'
