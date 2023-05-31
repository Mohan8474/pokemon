from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from app.config import Config

app = Flask(__name__)
# config = Config(app)
# config.read_config()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/pokemon"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


try:
    from app import views, models

    app.register_blueprint(views.pokemon_api)
except Exception as e:
    print(f"Error: {e}")
