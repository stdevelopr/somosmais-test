from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Somos +"

    return app