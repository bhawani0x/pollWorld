from api.Model.User import User
from flask import Blueprint, request
from flask.views import View
from api.Helper.helper import response
from flask_jwt_extended import create_access_token
from datetime import timedelta

login_bp = Blueprint("login", __name__)

expires_in = timedelta(minutes=10)


class Login(View):
    def dispatch_request(self):
        if request.method == 'POST':
            return self.login()

    def login(self):
        data = request.get_json()
        email = data.get("email")
        passwd = data.get("passwd")
        return self.userValidation(email, passwd)

    def userValidation(self, email, passwd):
        is_user_exists = User().get_user_by_email(email=email)
        if is_user_exists:
            if is_user_exists.check_passwd(passwd):
                access_token = create_access_token(identity=is_user_exists.id, expires_delta=expires_in)
                return response(msg=f'{access_token}', code=200)

        else:
            return response(msg="email-id or password not found", code=403)
