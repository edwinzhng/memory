from colorama import Fore

from src.display.Display import Display
from src.util.constants import CARDS_PER_ROW, MEMORY_ASCII, NUM_PAIRS

win_text = '''
  __   __            _    _ _       _ 
  \ \ / /           | |  | (_)     | |
   \ V /___  _   _  | |  | |_ _ __ | |
    \ // _ \| | | | | |/\| | | '_ \| |
    | | (_) | |_| | \  /\  / | | | |_|
    \_/\___/ \__,_|  \/  \/|_|_| |_(_)
'''

class GameDisplay(Display):
  def display(self, board, score, high_score,
                   matched, cur_card, selected,
                   is_match, show_match):
    print(self.term.move(*self.refresh_location))
    print('  Change cards with UP ↑, DOWN ↓, LEFT ←, RIGHT →\n')
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
    
    if show_match:
      if is_match:
        match_message = Fore.LIGHTGREEN_EX + 'You found a match!'
      else:
        match_message = Fore.LIGHTMAGENTA_EX + 'Try again!'
      print('\n  {} (Press any KEY to continue)'.format(match_message) + Fore.WHITE)
    else:
      print('\n                                                 ')
      
    print('\n  Score: {}       \n'.format(score))
    print('  High Score: {}      '.format(high_score))

  def display_game_over(self, score, high_score):
    print(self.term.move(*self.refresh_location))
    print(Fore.LIGHTGREEN_EX + win_text + Fore.WHITE)
    print('\n  Press ENTER to play again or press Q to quit.')
    print('\n\n  Score: {}'.format(score))
    print('  High Score: {}'.format(high_score))

  def is_flipped(self, row, col, matched, selected):
    return bool((row, col) in matched or (row, col) in selected)

  def is_selected(self, row, col, cur_card):
    return row == cur_card[0] and col == cur_card[1]
