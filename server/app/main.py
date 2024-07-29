import sys
from os import path
from flask import Flask
from flask_cors import CORS

ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.append(ROOT_FOLDER)

from app.routes.main_routes import main_blueprint
from app.routes.bot_routes import bot_blueprint

class Main:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.register_blueprints()

    def configure_app(self):
        CORS(self.app)

    def register_blueprints(self):
        self.app.register_blueprint(main_blueprint)
        self.app.register_blueprint(bot_blueprint, url_prefix='/bot')

    def run(self, debug=False):
        self.app.run(debug=debug)

if __name__ == '__main__':
    main = Main()
    main.app.run(debug=True)
