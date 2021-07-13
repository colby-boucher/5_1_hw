from flask import Flask
from config import Conf
from .main.routes import main
from .auth.routes import auth

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(auth)
app.config.from_object(Conf)