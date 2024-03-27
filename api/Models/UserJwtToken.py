from api.connection import db
from sqlalchemy.exc import IntegrityError
import datetime
# from api.Helper.helper import generate_log


class UserJwtTokens(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<JWT token for user : {self.id}"

    def get_user(self, id):
        return UserJwtTokens.query.get(id)

    def get_user_by_token(self, token):
        try:
            is_valid = UserJwtTokens.query.filter_by(token=token).first()
            if is_valid:
                return {'flag': True, 'msg': is_valid}
            else:
                return {'flag': False, 'msg': "Invalid token"}
        except Exception as e:
            # generate_log("CRITICAL", f"Connection Error ")
            return {'flag': False, 'msg': "An error occurred. Please try again."}

    def update_JWT_token(self, token):
        self.token = token
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def create_token(self, id, token):
        try:
            self.id = id
            self.token = token
            self.updated_at = datetime.datetime.utcnow()
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            generate_log("INFO", "Unable to create UserJwtTokens due to Integrity error")
            db.session.rollback()
        except Exception as e:
            db.session.rollback()
            generate_log("CRITICAL", f"Unable to create UserJwtTokens due to {e}")

    def delete_token(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            generate_log("CRITICAL", "Unable to delete UserJwtTokens due to Integrity error")
        except Exception as e:
            db.session.rollback()
            generate_log("CRITICAL", f"Unable to delete UserJwtTokens due to {e}")
            return False
        return True
