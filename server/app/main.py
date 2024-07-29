from flask import Flask
from config.constants import BOT_NAME, DATA_PATH
from routes.main_routes import main_blueprint
from routes.bot_routes import bot_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(bot_blueprint, url_prefix='/bot')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
