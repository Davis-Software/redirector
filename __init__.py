import os

from flask import Flask
from datetime import timedelta

from tools.config import Config
from flask_sqlalchemy import SQLAlchemy
from database import database_connection


working_dir = os.path.dirname(os.path.realpath(__file__))
config = Config(os.path.join(working_dir, 'config.ini'))

app = Flask(__name__)
db = SQLAlchemy()

app.secret_key = config.get("SECRET_KEY")
app.permanent_session_lifetime = timedelta(weeks=1)
database_connection.connect_to_database(
    app,
    database_connection.ConnectionProfile(
        config["DB_HOST"],
        config["DB_PORT"],
        config["DB_NAME"],
        config["DB_USER"],
        config["DB_PASS"],
        config["DB_TYPE"]
    ),
    {}
)
db.init_app(app)
""":type: sqlalchemy.orm"""

with app.app_context():
    from tools.route_loader import load_routes

    load_routes(working_dir, "routes")

    db.create_all()