from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import & Register Blueprints (Routes)
    from app.routes.item_routes import item_bp
    from app.swagger import swagger_bp  # Tambahkan Swagger

    app.register_blueprint(item_bp, url_prefix='/api/items')
    app.register_blueprint(swagger_bp, url_prefix='/swagger')  # Register Swagger

    return app
