from cards import Card, make_deck
from rules import *

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        deck = make_deck()
        self.trump_card = self.deck.pop() #dz randomly select a trump card from the deck
        self.trump = self.trump_card.mast
        self.deck = deck
        self.player = [self.deck.pop() for _ in range(6)]
        self.bot_cards = [self.deck.pop() for _ in range(6)]
        self.sort_hands()
        self.pairs = []
        self.message = ""
        self.winner = None
        self.turn = self._who_starts()
        self.awayting_more = False
        self.update_message()
    def sort_hands(self):
        def key(card):
            return (0 if card.mast != self.trump else 1, card.value)
        self.player.sort(key=key)
        self.bot_cards.sort(key=key)
    def _who_starts(self):
        player_trumps = [card.value for card in self.player if card.mast == self.trump]
        bot_trumps = [card.value for card in self.bot_cards if card.mast == self.trump]
        if player_trumps and bot_trumps:
            return min(player_trumps) < min(bot_trumps)
        if player_trumps:
            return True
        if bot_trumps:
            return False
        return True #придумтаь логику кто первий ходит, если у обоих нет козырей

    def update_message(self):
        if self.winner == "player":
            self.message = "You win!"
        if self.winner == "bot":
            self.message = "Bot wins!"
        if not self.pairs:
            self.message = "Your turn"
        else:
            self.message = "Bot's turn"
        
        if self.turn:
            if all_beaten(self.pairs):
                self.message = "Your turn"
            else:
                self.message = "Defend the attack"
        if all_beaten(self.pairs) and not self.turn:
            self.message = "Bot's turn"
        else:
            self.message = "Defend the attack or take the cards"
    
    def check_winner(self):
        if self.deck or self.trump_card is not None:
            return
        player_empty = not self.player
        bot_empty = not self.bot_cards
        if player_empty and bot_empty:
            self.winner = "draw"
        elif player_empty:
            self.winner = "player"
        elif bot_empty:
            self.winner = "bot"