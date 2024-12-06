import random

class BlackJack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        random.shuffle(self.deck)

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            {"value": "2", "points": 2}, {"value": "3", "points": 3}, {"value": "4", "points": 4},
            {"value": "5", "points": 5}, {"value": "6", "points": 6}, {"value": "7", "points": 7},
            {"value": "8", "points": 8}, {"value": "9", "points": 9}, {"value": "10", "points": 10},
            {"value": "JACK", "points": 10}, {"value": "QUEEN", "points": 10}, {"value": "KING", "points": 10},
            {"value": "ACE", "points": 11}
        ]
        return [{"value": value["value"], "suit": suit, "points": value["points"]} for suit in suits for value in values]

    def deal_card(self):
        return self.deck.pop()

    def start_game(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def hand_value(self, hand):
        value = sum(card["points"] for card in hand)
        aces = sum(1 for card in hand if card["value"] == "ACE")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def player_hit(self):
        self.player_hand.append(self.deal_card())
        return self.hand_value(self.player_hand)

    def dealer_turn(self):
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
        return self.hand_value(self.dealer_hand)

    def check_winner(self):
        player_value = self.hand_value(self.player_hand)
        dealer_value = self.hand_value(self.dealer_hand)
        if player_value > 21:
            return "Dealer wins! Player busted."
        elif dealer_value > 21:
            return "Player wins! Dealer busted."
        elif player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"