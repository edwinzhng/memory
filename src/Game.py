import random
import sys

from src.Card import Card
from src.display.GameDisplay import GameDisplay
from src.util.constants import CARDS_PER_ROW, NUM_PAIRS
from src.util.enums import CardValue, Difficulty, Suit


class Game():
  def __init__(self, terminal, difficulty):
    self.difficulty = difficulty
    self.term = terminal
    self.deck = [Card(value, suit) for value in CardValue for suit in Suit]
    self.high_score = 0
    self.display = GameDisplay(terminal)
    self.reset()
    self.seen = {}

  def run(self):
    while(True):
      self.reset()
      with self.term.fullscreen():
        self.display.print_header()
        self.refresh_display()

        # while not game over, prompt user for new selections
        while len(self.matched) < NUM_PAIRS * 2:
          self.select_cards()

      with self.term.fullscreen():
        if self.score > self.high_score:
          self.high_score = self.score

        self.display.print_header()
        self.display.display_game_over(self.score, self.high_score)

      with self.term.cbreak():
        key = ''
        while key.lower() != 'q' and getattr(key, 'name', '') != 'KEY_ENTER':
          key = self.term.inkey()
        if key.lower() == 'q':
          sys.exit()

  def reset(self) -> None:
    cards = random.sample(self.deck, NUM_PAIRS) * 2
    random.shuffle(cards)
    self.board = [cards[i:i+CARDS_PER_ROW] for i in range(0, NUM_PAIRS * 2, CARDS_PER_ROW)]
    self.selected = []
    self.matched = []
    self.cur_card = (0, 0)
    self.score = 0

  # select 2 cards and check if there is a match
  def select_cards(self):
    self.selected = []
    self.reset_cur_card()

    with self.term.cbreak():
      key = None
      while not key or key.name != 'KEY_ENTER':
        key = self.term.inkey()
        self.change_card(key)

      self.selected = [self.cur_card]
      self.reset_cur_card()
      key = None

      while not key or key.name != 'KEY_ENTER':
        key = self.term.inkey()
        self.change_card(key)

    self.selected.append(self.cur_card)
    self.refresh_display()
    self.move()

  # makes a move using the selected cards and updates matches if successful
  def move(self):
    score_diff = self.calculate_score()
    is_match = score_diff > 0
    if is_match:
      self.matched.extend(self.selected)

    is_match = score_diff > 0
    self.score += score_diff
    self.refresh_display(is_match, True)
  
    with self.term.cbreak():
      key = None
      while not key:
        key = self.term.inkey()

    for selection in self.selected:
      seen_row, seen_col = selection
      seen_card = self.board[seen_row][seen_col]
      if seen_card in self.seen:
        self.seen[seen_card].append((seen_row, seen_col))
      else:
        self.seen[seen_card] = [(seen_row, seen_col)]
    self.refresh_display()

  # sets cur_card to first unselected or unmatched card
  def reset_cur_card(self):
    for row in range(len(self.board), -1, -1):
      for col in range(CARDS_PER_ROW):
        if self.open_position(row, col):
          self.cur_card = (row, col)
          break
    self.refresh_display()

  # updates current selected card location based on keyboard input
  def change_card(self, key):
    if key.name not in ['KEY_UP', 'KEY_DOWN', 'KEY_LEFT', 'KEY_RIGHT']:
      return

    new_position = None
    is_row = True if key.name in ['KEY_UP', 'KEY_DOWN'] else False
    direction = 1 if key.name in ['KEY_DOWN', 'KEY_RIGHT'] else -1
    new_position = self.direction_has_open_position(is_row, direction)

    if not new_position:
      new_position = self.find_nearest_open_position(is_row, direction)

    if new_position:
      self.cur_card = new_position
      self.refresh_display()

  # check if already matched cards can be skipped and move selection
  def direction_has_open_position(self, is_row, direction):
    row, col = self.cur_card

    if is_row and (row + direction < 0 or row + direction >= len(self.board)):
      return self.cur_card
    elif not is_row and (col + direction < 0 or col + direction >= CARDS_PER_ROW):
      return self.cur_card

    if is_row:
      row += direction
      while row >= 0 and row < len(self.board):
        if self.open_position(row, col):
          return (row, col)
        row += direction
    else:
      col += direction
      while col >= 0 and col < CARDS_PER_ROW:
        if self.open_position(row, col):
          return (row, col)
        col += direction

    return None

  # finds next closest card diagonally if there is
  # no possible move along the specified direction
  def find_nearest_open_position(self, is_row, direction):
    row, col = self.cur_card
    if is_row:
      while 0 <= col + direction < CARDS_PER_ROW:
        position = None
        col += direction
    else:
      while 0 <= row + direction < len(self.board):
        position = None
        row += direction
    return None

  def refresh_display(self, is_match=False, show_match=False):
    self.display.display(self.board, self.score,
                         self.high_score, self.matched,
                         self.cur_card, self.selected,
                         is_match, show_match)

  # checks if a position is open to be selected
  def open_position(self, row, col) -> bool:
    return (row, col) not in self.matched and (row, col) not in self.selected

  # calculates score of selection based on difficulty
  def calculate_score(self):
    first, second = self.selected
    first_card = self.board[first[0]][first[1]]
    second_card = self.board[second[0]][second[1]]

    if first_card == second_card:
      return 1 if self.difficulty == Difficulty.NORMAL else 3

    # if second guess has already been seen in the same position
    # or if either card already has a known pair
    if (second_card in self.seen and second in self.seen[second_card]) or \
       (first_card in self.seen and len(self.seen[first_card]) == 2) or \
       (second_card in self.seen and len(self.seen[second_card]) == 2):
      return -1 if self.difficulty == Difficulty.NORMAL else -2

    return 0 if self.difficulty == Difficulty.NORMAL else -1
