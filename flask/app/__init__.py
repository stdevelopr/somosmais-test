import os
from flask import Flask
from .load_data import build_df

df = build_df()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    # import the routes
    from .views.clients import clients_bp
    app.register_blueprint(clients_bp)

    return app