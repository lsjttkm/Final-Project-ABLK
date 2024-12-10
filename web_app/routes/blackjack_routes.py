from flask import Blueprint, jsonify, render_template
from app.blackjack import BlackJack

blackjack_bp = Blueprint("routes", __name__)
game = None  # Initialize the game object globally

@blackjack_bp.route("/play/blackjack")
def blackjack():
    return render_template("blackjack_page.html")

@blackjack_bp.route("/start", methods=["POST"])
def start():
    global game
    game = BlackJack()
    game.start_game()
    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "dealer_hand": [{"value": game.dealer_hand[0]["value"], "suit": game.dealer_hand[0]["suit"]}, "Hidden"],
        "player_value": game.get_hand_value(game.player_hand),
        "dealer_value": game.get_hand_value([game.dealer_hand[0]])
    })

@blackjack_bp.route("/hit", methods=["POST"])
def hit():
    global game
    if not game:
        return jsonify({"error": "Game not started"}), 400

    player_value = game.player_hit()
    if player_value > 21:
        return jsonify({
            "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
            "player_value": player_value,
            "result": "Dealer wins! Player busted."
        })

    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "player_value": player_value
    })

@blackjack_bp.route("/stand", methods=["POST"])
def stand():
    global game
    if not game:
        return jsonify({"error": "Game not started"}), 400

    dealer_value = game.dealer_turn()
    result = game.check_winner()
    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "player_value": game.get_hand_value(game.player_hand),
        "dealer_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.dealer_hand],
        "dealer_value": dealer_value,
        "result": result
    })