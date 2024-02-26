from api.app import app
from flask_sqlalchemy import SQLAlchemy
from api.settings import MYSQL_DB_CONNECTION

app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_DB_CONNECTION

# Initialize SQLAlchemy instance
db = SQLAlchemy(app=app)
