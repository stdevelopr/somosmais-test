import os
from flask import Flask
from .load_data import build_df

df = build_df()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    # load the test config if passed in
    if test_config:
        app.config.from_mapping(test_config)

    # import the routes
    from .views.clients import clients_bp
    app.register_blueprint(clients_bp)

    return app