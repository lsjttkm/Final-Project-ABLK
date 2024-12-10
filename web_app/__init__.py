from flask import Flask

def create_app():
    # Specify the `template_folder` for HTML templates
    app = Flask(__name__, template_folder="templates")
    
    from web_app.routes.home_routes import home_bp
    from web_app.routes.blackjack_routes import blackjack_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(blackjack_bp)
    return app

# Create an app instance for Flask CLI
app = create_app()