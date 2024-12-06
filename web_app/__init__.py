from flask import Flask

def create_app():
    # Specify the `template_folder` for HTML templates
    app = Flask(__name__, template_folder="templates")
    from web_app.routes import bp
    app.register_blueprint(bp)
    return app

# Create an app instance for Flask CLI
app = create_app()