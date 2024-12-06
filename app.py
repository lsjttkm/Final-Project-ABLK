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
    game = BlackJack()
    game.start_game()
    return jsonify({
        "player_hand": [{"value": card["value"], "suit": card["suit"]} for card in game.player_hand],
        "dealer_hand": [{"value": game.dealer_hand[0]["value"], "suit": game.dealer_hand[0]["suit"]}, "Hidden"],
        "player_value": game.get_hand_value(game.player_hand),
        "dealer_value": game.get_hand_value([game.dealer_hand[0]])  # Only the first card is visible
    })



@app.route("/hit", methods=["POST"])
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

@app.route("/stand", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)