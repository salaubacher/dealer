""" Deck module """

import random


class Deck:
    """A deck of any style playing cards with 2 attributes"""

    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f"{suit}{value}")

    def shuffle(self):
        """Randomly reorder the deck. Based on:
        https://www.nytimes.com/1990/01/09/science/in-shuffling-cards-7-is-winning-number.html
        the deck will be shuffled 7 times
        """
        for i in range(7):
            for i in range(len(self.deck) - 1):
                index = random.randint(0, len(self.deck) - 1)
                if index != i:
                    self.deck[index], self.deck[i] = (
                        self.deck[i],
                        self.deck[index],
                    )

    def deal_one_card(self):
        """Return the card from the “top” of the deck to the caller;
        If the deck is empty, no card is dealt.
        """
        if len(self.deck) > 0:
            return self.deck.pop()
        return None

    def card_count(self):
        """Return the number of cards in the deck"""
        return len(self.deck)

    def __str__(self):
        return f"{self.deck}"

    def __eq__(self, other: object):
        if isinstance(self, other.__class__):
            return self.deck == other.deck  # type: ignore
        return False

    def __repr__(self):
        return f"Deck(deck={repr(self.deck)})"
