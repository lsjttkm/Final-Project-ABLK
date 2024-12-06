from flask import Flask, jsonify, send_file
from blackjack import BlackJack

app = Flask(__name__, static_folder="static")
game = None  # Initialize the game object globally


@app.route("/")
def index():
    # Serve the static HTML file
    return send_file("static/index.html")


@app.route("/start", methods=["POST"])
def start():
    global game
    game = BlackJack()  # Start a new game
    game.start_game()  # Deal initial cards

    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "dealer_hand": [{"value": game.dealer_hand[0]["value"], "suit": game.dealer_hand[0]["suit"]}, "Hidden"]
    })


@app.route("/hit", methods=["POST"])
def hit():
    global game
    if not game:
        return jsonify({"error": "Game not started"}), 400

    # Player draws a card
    player_value = game.player_hit()

    # Check if player busts
    if player_value > 21:
        return jsonify({
            "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
            "result": "Dealer wins! Player busted."
        })

    # Otherwise, continue game
    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand]
    })


@app.route("/stand", methods=["POST"])
def stand():
    global game
    if not game:
        return jsonify({"error": "Game not started"}), 400

    # Dealer's turn
    dealer_value = game.dealer_turn()
    result = game.check_winner()

    # Reveal all cards and return the result
    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "dealer_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.dealer_hand],
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)