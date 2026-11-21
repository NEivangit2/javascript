from random import random

COLODA = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
MAST = ['♠', '♥', '♦', '♣']

red_mast = ['♥', '♦']
black_mast = ['♠', '♣']

class Card:
    def __init__(self, mast, rank):
        self.mast = mast
        self.rank = rank

    @property
    def value(self):
        return coloda.index(self.rank)
    @property
    def is_red(self):
        return self.mast in red_mast

    def beats(self, other, trump):
        if self.mast == other.mast:
            return self.value > other.value
        return self.mast == trump and other.mast != trump

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __repr__(self):
        return f'{self.rank}{self.suit}'

def make_deck():
    cards = [Card(mast, rank) for mast in MAST for rank in COLODA]
    random.shuffle(cards)
    return cards