from os import path

ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))

BOT_NAME = "Cinebot"
DATA_PATH = [path.join(ROOT_FOLDER, "data/greetings.json"), path.join(ROOT_FOLDER, "data/questions.json"), path.join(ROOT_FOLDER, "data/basic-info.json")]
MINIMAL_CONFIDENCE = 0.5
DB_NAME = "db.sqlite3"