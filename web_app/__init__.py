from flask import Flask

from web_app.routes.home_routes import home_bp
from web_app.routes.blackjack_routes import blackjack_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(blackjack_bp)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)