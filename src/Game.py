import random

from src.Card import Card
from src.display.GameDisplay import GameDisplay
from src.util.constants import CARDS_PER_ROW, NUM_PAIRS
from src.util.enums import CardValue, Suit


class Game():
  def __init__(self, terminal, difficulty):
    self.difficulty = difficulty
    self.term = terminal
    self.deck = [Card(value, suit) for value in CardValue for suit in Suit]
    self.high_score = 0
    self.display = GameDisplay(terminal)
    self.reset()

  def run(self):
    while(True):
      self.reset()
      self.refresh_display()
      while len(self.matched) < NUM_PAIRS * 2:
        self.select_cards()
        self.move()
        self.refresh_display()
      
      self.display.display_game_over(self.score, self.high_score)

      with self.term.cbreak():
        key = None
        while not key or key.name not in ['KEY_ENTER', 'q', 'Q']:
            key = self.term.inkey()

        if key.name in ['q', 'Q']:
          break

  def reset(self) -> None:
    cards = random.sample(self.deck, NUM_PAIRS) * 2
    random.shuffle(cards)
    self.board = [cards[i:i+CARDS_PER_ROW] for i in range(0, NUM_PAIRS * 2, CARDS_PER_ROW)]
    self.selected = []
    self.matched = []
    self.cur_card = (0, 0)
    self.score = 0

  def refresh_display(self, is_match=False, show_match=False):
    self.display.display_game(self.board, self.score,
                         self.high_score, self.matched,
                         self.cur_card, self.selected,
                         is_match, show_match)

  def select_cards(self):
    self.selected = []
    self.reset_cur_card()

    with self.term.cbreak():
      key = None
      while not key or key.name is not 'KEY_ENTER':
        key = self.term.inkey()
        self.change_card(key)

      self.selected = [self.cur_card]
      self.reset_cur_card()

      while not key or key.name is not 'KEY_ENTER':
        key = self.term.inkey()
        self.change_card(key)

      self.selected = [self.selected[0], self.cur_card]

  def move(self):
    first, second = self.selected
    is_match = self.board[first[0]][first[1]] == self.board[second[0]][second[1]]

    self.refresh_display(is_match, True)
    with self.term.cbreak():
      key = None
      while not key or key.name is not 'KEY_ENTER':
        key = self.term.inkey()
        
    if is_match:
      self.score += 1
      if self.score > self.high_score:
        self.high_score = self.score

      self.matched.extend([first, second])

  def change_card(self, key):
    x, y = self.cur_card

    if x > 0 and key.name == 'KEY_UP':
      x -= 1
    elif x < NUM_PAIRS * 2 // CARDS_PER_ROW - 1 and key.name == 'KEY_DOWN':
      x += 1

    if y > 0 and key.name == 'KEY_LEFT':
      y -= 1
    elif y < CARDS_PER_ROW - 1 and key.name == 'KEY_RIGHT':
      y += 1

    self.cur_card = (x, y)
    self.refresh_display()

  # sets cur_card to first unselected or unmatched card
  def reset_cur_card(self):
    for row in range(NUM_PAIRS * 2 // CARDS_PER_ROW):
      for col in range(CARDS_PER_ROW):
        if self.board[row][col] \
           and ((row, col) not in self.selected or (row, col) not in self.matched):
          self.cur_card = (row, col)
          break
    self.refresh_display()