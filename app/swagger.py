from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Flask API"})

