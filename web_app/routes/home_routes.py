from flask import Blueprint, render_template, flash, redirect, url_for

home_bp = Blueprint("home_routes", __name__)

@home_bp.route("/")
@home_bp.route("/home")
def home():
    return render_template("home_page.html")

@home_bp.route("/play/<game_name>")
def play_game(game_name):
    if game_name == "blackjack":
        return redirect(url_for("blackjack_routes.blackjack"))
    else:
        flash(f"Sorry, {game_name.capitalize()} is not available right now!", "info")
        return redirect(url_for("home_routes.home"))