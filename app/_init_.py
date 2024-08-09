from flask import Flask
from .routes import password_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(password_routes)
    return app

