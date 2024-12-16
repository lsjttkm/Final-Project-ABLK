import requests

class BlackJack:
    def __init__(self):
        self.deck_id = None
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        if response.status_code == 200:
            self.deck_id = response.json()["deck_id"]
        else:
            raise Exception("Failed to create deck")

    def draw_cards(self, count):
        if not self.deck_id:
            self.create_deck()
        response = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}")
        if response.status_code == 200:
            return response.json()["cards"]
        else:
            raise Exception("Failed to draw cards")

    def start_game(self):
        self.create_deck()
        self.player_hand = self.draw_cards(2)
        self.dealer_hand = self.draw_cards(2)

    def get_hand_value(self, hand):
        values = {"ACE": 11, "KING": 10, "QUEEN": 10, "JACK": 10}
        value = 0
        aces = 0
        for card in hand:
            card_value = card["value"]
            if card_value.isdigit():
                value += int(card_value)
            else:
                value += values[card_value]
                if card_value == "ACE":
                    aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def player_hit(self):
        self.player_hand += self.draw_cards(1)
        return self.get_hand_value(self.player_hand)

    def dealer_turn(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand += self.draw_cards(1)
        return self.get_hand_value(self.dealer_hand)

    def check_winner(self):
        player_value = self.get_hand_value(self.player_hand)
        dealer_value = self.get_hand_value(self.dealer_hand)
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
    