from api.app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
db.init_app(app)
