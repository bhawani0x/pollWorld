from api.connection import db
from sqlalchemy.exc import IntegrityError


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.topic

    def all_topics(self):
        return Categories.query.all()

    def create(self, topic):
        try:
            self.topic = topic
            db.session.add(self)
            db.session.commit()
            return self

        except IntegrityError:
            db.session.rollback()
            return False  # Indicate failure due to unique constraint violation

        except Exception as e:
            db.session.rollback()
            print("An error occurred:", str(e))
            return False  # Indicate general failure
