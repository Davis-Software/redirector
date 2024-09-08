import os

from flask import Flask

from tools.config import Config
from flask_sqlalchemy import SQLAlchemy
from database import database_connection
from utils.scheduling import Scheduler


working_dir = os.path.dirname(os.path.realpath(__file__))
config = Config(os.path.join(working_dir, 'config/config.ini'))

app = Flask(__name__)
db = SQLAlchemy()

app.secret_key = config.get("SECRET_KEY")
database_connection.connect_to_database(
    app,
    database_connection.ConnectionProfile(
        config.get("DB_HOST"),
        config.get("DB_PORT"),
        config.get("DB_NAME"),
        config.get("DB_USER"),
        config.get("DB_PASS"),
        config.get("DB_TYPE")
    ),
    {}
)
db.init_app(app)
""":type: sqlalchemy.orm"""

scheduler = Scheduler(config)

with app.app_context():
    from tools.route_loader import load_routes

    load_routes(working_dir, "routes")
    db.create_all()

    scheduler.start()
