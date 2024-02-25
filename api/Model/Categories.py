from api.connection import db


class Categories(db.Model):
    topic = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.topic
