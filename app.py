from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


# Create the Flask app
app = Flask(__name__)


def index():
    return 'Hello, World!'