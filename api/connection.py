from api.app import app
from flask_sqlalchemy import SQLAlchemy
from api.settings import MYSQL_DB_CONNECTION
from flask_pymongo import PyMongo

app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_DB_CONNECTION
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'  # Set your MongoDB URI here

# Initialize SQLAlchemy instance
db = SQLAlchemy(app=app)

# Initialize MongoDB instance
mongo = PyMongo(app=app)
