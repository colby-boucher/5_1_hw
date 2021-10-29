from flask import Flask
from config import Conf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .main.routes import main
from .authentication.routes import auth

from .models import db

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(auth)
app.config.from_object(Conf)

db.init_app(app)

migrate = Migrate(app, db)

from . import models