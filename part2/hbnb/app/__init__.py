# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns  # Si tu utilises un namespace pour les utilisateurs

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Enregistre le namespace des utilisateurs (ou tout autre namespace que tu utilises)
    api.add_namespace(users_ns, path='/api/v1/users')

    return app