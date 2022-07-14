""" PockerDeck module """

from .deck import Deck


class PokerDeck(Deck):
    """A deck of poker-style playing cards:
    fifty-two playing cards in four suits: hearts, spades, clubs, diamonds,
    with face values of Ace, 2-10, Jack, Queen, and King.
    """

    suits = ["C", "D", "H", "S"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self):
        super().__init__(self.suits, self.values)
