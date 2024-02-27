import datetime
from api.connection import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

user_categories = db.Table('user_categories',
                           db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                           db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
                           )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum('Male', 'Female', 'Other'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Define relationship with categories
    categories = db.relationship('Categories', secondary=user_categories, backref='users')

    def __repr__(self):
        return self.username

    def create_user(self, name, username, email, password, mob_num, dob, gender):
        try:
            self.name = name
            self.username = username
            self.email = email
            self.password = generate_password_hash(password)
            self.mobile_number = mob_num
            self.dob = dob
            self.gender = gender

            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False  # Indicate failure due to unique constraint violation

        except Exception as e:
            db.session.rollback()
            print("An error occurred:", str(e))
            return False  # Indicate general failure

    def check_passwd(self, password):
        return check_password_hash(self.password, password)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()
