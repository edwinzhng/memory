from unittest.mock import Mock

from blessed import Terminal

from src.Card import Card
from src.Game import Game
from src.util.constants import CARDS_PER_ROW, NUM_PAIRS
from src.util.enums import CardValue, Difficulty, Suit


def test_score_increases_on_match():
    game = Game(Terminal(), Difficulty.NORMAL)
    matched_card = Card(CardValue.ACE, Suit.CLUBS)
    game.board[0][0] = matched_card
    game.board[0][1] = matched_card
    game.selected = [(0, 0), (0, 1)]

    assert game.calculate_score() == 1
    game.difficulty = Difficulty.HARD
    assert game.calculate_score() == 3

def test_score_wrong_match_when_entire_pair_already_seen():
    game = Game(Terminal(), Difficulty.NORMAL)
    card = Card(CardValue.ACE, Suit.CLUBS)
    other_card = Card(CardValue.TWO, Suit.HEARTS)
    game.board[0][0] = card
    game.board[0][1] = other_card
    game.selected = [(0, 0), (0, 1)]
    game.seen[card] = [(0, 0), (0, 2)]

    assert game.calculate_score() == -1
    game.difficulty = Difficulty.HARD
    assert game.calculate_score() == -2

def test_score_wrong_match_when_location_of_match_seen():
    game = Game(Terminal(), Difficulty.NORMAL)
    card = Card(CardValue.ACE, Suit.CLUBS)
    other_card = Card(CardValue.TWO, Suit.HEARTS)
    game.board[0][0] = card
    game.board[0][1] = other_card
    game.selected = [(0, 0), (0, 1)]
    game.seen[card] = [(0, 2)]

    assert game.calculate_score() == -1
    game.difficulty = Difficulty.HARD
    assert game.calculate_score() == -2

def test_score_wrong_match_second_card_when_card_already_seen():
    game = Game(Terminal(), Difficulty.NORMAL)
    seen_card = Card(CardValue.TWO, Suit.HEARTS)
    game.board[0][0] = Card(CardValue.ACE, Suit.CLUBS)
    game.board[0][1] = seen_card
    game.selected = [(0, 0), (0, 1)]
    game.seen[seen_card] = [(0, 1)]

    assert game.calculate_score() == -1
    game.difficulty = Difficulty.HARD
    assert game.calculate_score() == -2

def test_score_wrong_match_and_card_not_already_seen():
    game = Game(Terminal(), Difficulty.NORMAL)
    game.board[0][0] = Card(CardValue.THREE, Suit.SPADES)
    game.board[0][1] = Card(CardValue.TWO, Suit.HEARTS)
    game.selected = [(0, 0), (0, 1)]

    assert game.calculate_score() == 0
    game.difficulty = Difficulty.HARD
    assert game.calculate_score() == -1

def test_move_sets_correct_seen_values():
    game = Game(Terminal(), Difficulty.NORMAL)
    card = Card(CardValue.THREE, Suit.SPADES)
    other_card = Card(CardValue.TWO, Suit.HEARTS)
    game.board[0][0] = card
    game.board[0][1] = other_card
    game.selected = [(0, 0), (0, 1)]
    game.seen[card] = [(0, 2)]
    game.move(False)

    assert game.seen[card] == [(0, 2), (0, 0)]
    assert game.seen[other_card] == [(0, 1)]
    seen = game.seen
    game.selected = [(0, 0), (0, 1)]
    game.move(False)
    assert game.seen == seen

def test_move_sets_matched_cards_correctly():
    game = Game(Terminal(), Difficulty.NORMAL)
    card = Card(CardValue.THREE, Suit.SPADES)
    game.board[0][0] = card
    game.board[0][1] = card
    game.selected = [(0, 0), (0, 1)]
    game.move(False)

    assert (0, 0) in game.matched
    assert (0, 1) in game.matched

def test_change_card_works_properly():
    game = Game(Terminal(), Difficulty.NORMAL)
    game.cur_card = (2, 2)
    key = Mock()

    key.name = 'KEY_UP'
    game.change_card(key)
    assert game.cur_card == (1, 2)

    key.name = 'KEY_LEFT'
    game.change_card(key)
    assert game.cur_card == (1, 1)

    key.name = 'KEY_DOWN'
    game.change_card(key)
    assert game.cur_card == (2, 1)

    key.name = 'KEY_RIGHT'
    game.change_card(key)
    assert game.cur_card == (2, 2)

def test_change_card_does_nothing_at_borders():
    game = Game(Terminal(), Difficulty.NORMAL)
    key = Mock()

    key.name = 'KEY_UP'
    game.cur_card = (0, 0)
    game.change_card(key)
    assert game.cur_card == (0, 0)

    key.name = 'KEY_LEFT'
    game.change_card(key)
    assert game.cur_card == (0, 0)

    key.name = 'KEY_DOWN'
    game.cur_card = (3, 4)
    game.change_card(key)
    assert game.cur_card == (3, 4)

    key.name = 'KEY_RIGHT'
    game.change_card(key)
    assert game.cur_card == (3, 4)

def test_change_card_skips_matched_cards():
    game = Game(Terminal(), Difficulty.NORMAL)
    game.cur_card = (2, 2)
    key = Mock()
    game.matched = [(1, 2), (0, 1), (1, 0),
                    (2, 0), (3, 1), (3, 2)]

    key.name = 'KEY_UP'
    game.change_card(key)
    assert game.cur_card == (0, 2)

    key.name = 'KEY_LEFT'
    game.change_card(key)
    assert game.cur_card == (0, 0)

    key.name = 'KEY_DOWN'
    game.change_card(key)
    assert game.cur_card == (3, 0)

    key.name = 'KEY_RIGHT'
    game.change_card(key)
    assert game.cur_card == (3, 3)

def test_change_card_goes_to_nearest_open_card_when_blocked():
    game = Game(Terminal(), Difficulty.NORMAL)
    key = Mock()

    key.name = 'KEY_UP'
    game.cur_card = (3, 4)
    game.matched = [(0, 4), (1, 4), (2, 4)]
    game.change_card(key)
    assert game.cur_card == (2, 3)

    key.name = 'KEY_LEFT'
    game.cur_card = (0, 4)
    game.matched = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4)]
    game.change_card(key)
    assert game.cur_card == (1, 3)

    key.name = 'KEY_DOWN'
    game.cur_card = (0, 0)
    game.matched = [(0, 1), (1, 0), (2, 0), (3, 0), (0, 2)]
    game.change_card(key)
    assert game.cur_card == (1, 1)

    key.name = 'KEY_RIGHT'
    game.cur_card = (0, 0)
    game.matched = [(0, 1), (1, 0), (0, 2), (0, 3), (0, 4)]
    game.change_card(key)
    assert game.cur_card == (1, 1)

def test_change_card_does_not_go_out_of_bounds_when_blocked():
    game = Game(Terminal(), Difficulty.NORMAL)
    key = Mock()

    key.name = 'KEY_RIGHT'
    game.cur_card = (2, 2)
    game.matched = [(2, 3), (2, 4), (3, 2), (3, 3),
                    (1, 3), (1, 4), (0, 3), (0, 4)]
    game.change_card(key)
    assert game.cur_card == (3, 4)

    key.name = 'KEY_RIGHT'
    game.cur_card = (0, 0)
    game.matched = [(0, 1), (0, 2), (0, 3), (0, 4),
                    (1, 1), (1, 2), (1, 3), (1, 4),
                    (2, 1), (2, 2), (2, 3), (2, 4),
                    (3, 1), (3, 2), (3, 3)]
    game.change_card(key)
    assert game.cur_card == (3, 4)

def test_reset_cur_card():
    game = Game(Terminal(), Difficulty.NORMAL)
    game.selected = [(0, 0)]
    game.matched = [(0, 1), (0, 2)]
    game.reset_cur_card()

    assert game.cur_card == (0, 3)

def test_reset():
    game = Game(Terminal(), Difficulty.NORMAL)
    game.selected = [(0,0)]
    game.matched = [(1, 0), (2, 2)]
    game.high_score = 10
    game.score = 2
    game.reset()

    assert game.score == 0
    assert game.high_score == 10
    assert game.matched == []
    assert game.selected == []
    assert len(game.board) == NUM_PAIRS * 2 // CARDS_PER_ROW
    assert len(game.board[0]) == CARDS_PER_ROW
