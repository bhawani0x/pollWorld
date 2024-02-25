from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# JWT Setup
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)
