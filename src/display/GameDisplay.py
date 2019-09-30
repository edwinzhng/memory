from colorama import Fore

from src.display.Display import Display
from src.util.constants import CARDS_PER_ROW, MEMORY_ASCII, NUM_PAIRS


class GameDisplay(Display):
  def display(self, board, score, high_score,
                   matched, cur_card, selected,
                   is_match, show_match):
    with self.term.fullscreen():
      self.print_header()
      print(self.term.move(*self.refresh_location))
      print('  Change cards with UP ↑, DOWN ↓, LEFT ←, RIGHT →\n\n')
      print('  Press ENTER to select a card')
      
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

      print('\n')
      if show_match:
        if is_match:
          match_message = Fore.LIGHTGREEN_EX + 'You found a match!'
        else:
          match_message = Fore.LIGHTMAGENTA_EX + 'Try again!'
        print('  {} (Press any KEY to continue)'.format(match_message) + Fore.RESET)
      else:
        print()
      print('\n  Score: {}       \n'.format(score))
      print('  High Score: {}      '.format(high_score))

  def display_game_over(self, score, high_score):
    with self.term.fullscreen():
      self.print_header()
      print(self.term.move(*self.refresh_location))
      print('\n\n  You won! Press ENTER to play again or press Q to quit.')
      print('\n\n  Score: {}'.format(score))
      print('  High Score: {}'.format(high_score))

  def is_flipped(self, row, col, matched, selected):
    return bool((row, col) in matched or (row, col) in selected)

  def is_selected(self, row, col, cur_card):
    return row == cur_card[0] and col == cur_card[1]
