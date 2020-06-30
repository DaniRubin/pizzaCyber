from flask.ext.sqlalchemy import SQLAlchemy
from app_factory import app

db = SQLAlchemy(app)