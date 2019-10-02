from colorama import Fore

from src.Card import Card
from src.util.enums import CardValue, Suit


def test_card_clubs():
    card = Card(CardValue.ACE, Suit.CLUBS)
    assert card.value == CardValue.ACE
    assert card.suit == Suit.CLUBS
    assert card.color == Fore.LIGHTCYAN_EX
    assert str(card) == "{}{}{}".format(card.color, 'A♣', Fore.WHITE)

def test_card_diamonds():
    card = Card(CardValue.JACK, Suit.DIAMONDS)
    assert card.value == CardValue.JACK
    assert card.suit == Suit.DIAMONDS
    assert card.color == Fore.LIGHTRED_EX
    assert str(card) == "{}{}{}".format(card.color, 'J♦', Fore.WHITE)

def test_card_hearts():
    card = Card(CardValue.QUEEN, Suit.HEARTS)
    assert card.value == CardValue.QUEEN
    assert card.suit == Suit.HEARTS
    assert card.color == Fore.LIGHTRED_EX
    assert str(card) == "{}{}{}".format(card.color, 'Q♥', Fore.WHITE)

def test_card_spades():
    card = Card(CardValue.KING, Suit.SPADES)
    assert card.value == CardValue.KING
    assert card.suit == Suit.SPADES
    assert card.color == Fore.LIGHTCYAN_EX
    assert str(card) == "{}{}{}".format(card.color, 'K♠', Fore.WHITE)

def test_card_equality():
    card = Card(CardValue.KING, Suit.SPADES)
    assert not (card == Card(CardValue.KING, Suit.HEARTS))
    assert card == Card(CardValue.KING, Suit.SPADES)

def test_card_hashable():
    card = Card(CardValue.KING, Suit.SPADES)
    assert card.__hash__() == hash("KING of SPADES")
