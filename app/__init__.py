from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import Config

app = Flask(__name__)
config = Config(app)
# print(config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


try:
    from app import views, models

    app.register_blueprint(views.pokemon_api)
except Exception as e:
    print(f"Error: {e}")
