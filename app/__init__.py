#installed imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
# from flask_jwt_extended import JWTManager

#custom imports
from app.config import Config

app = Flask(__name__)
config = Config(app)

# app.config['JWT_SECRET_KEY'] = 'your-secret-key'
# jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
app.secret_key = "mohan"

try:
    from app import views, models, auth

    app.register_blueprint(views.pokemon_api)
except Exception as e:
    print(f"Error: {e}")

# def create_app():
#     app = Flask(__name__)
#     config = Config(app)

#     db.init_app(app)
#     migrate.init_app(app,db)
#     ma.init_app(app)

#     from app import views, models, auth

#     app.register_blueprint(views.pokemon_api)

#     return app
