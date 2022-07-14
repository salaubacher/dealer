from dealer.poker_deck import PokerDeck


class TestPokerDeck:
    def test_card_count(self):
        poker_deck = PokerDeck()
        print("testing Card Count")
        assert poker_deck.card_count() == 52

    def test_deal_one_card(self):
        poker_deck = PokerDeck()
        print("testing deal one card")
        assert poker_deck.card_count() == 52
        top_card = poker_deck.deal_one_card()
        assert top_card is not None
        assert top_card == "SA"
        assert poker_deck.card_count() == 51
        for _ in range(51):
            poker_deck.deal_one_card()
        top_card = poker_deck.deal_one_card()
        assert top_card is None

    def test_shuffle(self):
        unshuffled = PokerDeck()
        poker_deck = PokerDeck()
        assert poker_deck == unshuffled
        print("testing shuffle")
        poker_deck.shuffle()
        assert poker_deck != unshuffled

    def test_deal_all(self):
        poker_deck = PokerDeck()
        print("test dealing all cards")
        poker_deck.shuffle()
        for _ in range(52):
            poker_deck.deal_one_card()
        assert poker_deck.card_count() == 0

    def test_deck_equality(self):
        poker_deck1 = PokerDeck()
        poker_deck2 = PokerDeck()
        assert poker_deck1 == poker_deck2
        assert poker_deck1 != "string"
