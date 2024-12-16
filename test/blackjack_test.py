import pytest
from app.blackjack import BlackJack

@pytest.fixture
def blackjack_game():
    """Fixture to create a BlackJack game instance."""
    game = BlackJack()
    game.create_deck()  # Ensure a deck is created for all tests
    return game

def test_create_deck(blackjack_game):
    """Test deck creation."""
    assert blackjack_game.deck_id is not None, "Deck ID should be initialized."

def test_draw_cards(blackjack_game):
    """Test drawing cards."""
    cards = blackjack_game.draw_cards(2)
    assert len(cards) == 2, "Should draw 2 cards."
    assert all("value" in card and "suit" in card for card in cards), "Cards should have value and suit."

def test_start_game(blackjack_game):
    """Test starting a game."""
    blackjack_game.start_game()
    assert len(blackjack_game.player_hand) == 2, "Player should have 2 cards."
    assert len(blackjack_game.dealer_hand) == 2, "Dealer should have 2 cards."

def test_get_hand_value():
    """Test calculating hand value."""
    game = BlackJack()
    hand = [{"value": "10", "suit": "HEARTS"}, {"value": "ACE", "suit": "SPADES"}]
    value = game.get_hand_value(hand)
    assert value == 21, "Hand value should be 21 with 10 and ACE."

def test_player_hit(blackjack_game):
    """Test player hit action."""
    blackjack_game.start_game()
    initial_hand_size = len(blackjack_game.player_hand)
    blackjack_game.player_hit()
    assert len(blackjack_game.player_hand) == initial_hand_size + 1, "Player hand should increase by 1."

def test_check_winner(blackjack_game):
    """Test checking the winner."""
    blackjack_game.player_hand = [{"value": "10", "suit": "HEARTS"}, {"value": "10", "suit": "SPADES"}]
    blackjack_game.dealer_hand = [{"value": "9", "suit": "DIAMONDS"}, {"value": "8", "suit": "CLUBS"}]
    result = blackjack_game.check_winner()
    assert result == "Player wins!", "Player should win with a higher hand value."