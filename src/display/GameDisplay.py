from colorama import Fore

from src.util.constants import CARDS_PER_ROW, NUM_PAIRS, MEMORY_ASCII


class GameDisplay:
  def __init__(self, terminal):
    self.term = terminal

  def display_game(self, board, score, high_score,
                   matched, cur_card, selected,
                   is_match, show_match):
    self.term.clear()
    with self.term.fullscreen():
      print(Fore.LIGHTCYAN_EX + MEMORY_ASCII + Fore.RESET + '\n')
      x, y = self.term.get_location()
      y_0 = y

      for row_idx, row in enumerate(board):
        for col_idx, card in enumerate(row):
          card.display(self.term, (x, y),
                       flipped=self.is_flipped(row_idx, col_idx, matched, selected),
                       selected=self.is_selected(row_idx, col_idx, cur_card))
          y += 8

        y = y_0
        x += 5

      print('\n\n')

      if show_match:
        match_message = 'You found a match!' if is_match else 'Try again!'
        print('{}'.format(match_message))
      else:
        print()

      print('  Score: {}'.format(score))
      print('  High Score: {}'.format(high_score))

  
  def display_game_over(self, score, high_score):
    self.term.clear()
    with self.term.fullscreen():
      print(Fore.LIGHTCYAN_EX + memory_ascii + Fore.RESET + '\n')
      print('\n\n  You won! Press ENTER to play again or press Q to quit.')

      print('\n\n  Score: {}'.format(score))
      print('  High Score: {}'.format(high_score))

  def is_flipped(self, row, col, matched, selected):
    return bool((row, col) in matched or (row, col) in selected)

  def is_selected(self, row, col, cur_card):
    return row is cur_card[0] and col is cur_card[1]

