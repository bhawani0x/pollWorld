from datetime import timedelta

from flask import request, Blueprint
from flask.views import View
from flask_jwt_extended import create_access_token, get_jti, get_jwt_identity

from api.Decorators.verify_user import valid_jti_required
from api.Helper.helper import response, generate_log
from api.Helper.validation import Validation
from api.Models.UserJwtToken import UserJwtTokens
from api.Models.User import User
from api.settings import JWT_TOKEN_EXP

login_bp = Blueprint('login_bp', __name__)

# Set custom timeout for jwt token
expires_in = timedelta(minutes=int(JWT_TOKEN_EXP))


class Login(View):

    def dispatch_request(self):
        if request.method == 'POST':
            data = request.get_json()
            reset_token = data.get('reset_token', False)
            if reset_token:
                return self.__login(data, reset_token=True)
            return self.__login(data)
        elif request.method == 'DELETE':
            return self.logout()

    def __login(self, data, reset_token=False):
        # validate data and captcha response
        check = self.__check_data(data.get('email'), data.get('password'))

        if not check['flag']:
            return response(msg=check['msg'], code=check['code'])

        email = data.get('email').lower()
        try:
            user = User()
            is_user_exists = user.get_user_by_email(email=email)
            if is_user_exists:
                # if is_user_exists.email_verified_at is None:
                #     return response(msg="Please Verify your email", code=400)
                if not is_user_exists.check_passwd(data.get('password')):
                    return response(msg="Invalid email or password", code=401)
                else:
                    userJwtToken = UserJwtTokens()
                    is_token_exists = userJwtToken.get_user(id=is_user_exists.id)
                    if is_token_exists is None:  # CREATE JWT Token
                        access_token = create_access_token(identity=is_user_exists.id, expires_delta=expires_in)
                        userJwtToken.create_token(id=is_user_exists.id, token=get_jti(access_token))
                        return response(msg=f'{access_token}', code=200)
                    elif is_token_exists and reset_token:  # UPDATE JWT Token
                        access_token = create_access_token(identity=is_user_exists.id, expires_delta=expires_in)
                        is_token_exists.update_JWT_token(token=get_jti(access_token))
                        return response(msg=f'{access_token}', code=200)
                    else:
                        return response(msg='you already have active session please logout first', code=403)
            else:
                return response(msg="Please register your account", code=401)
        except Exception as e:
            if 'OperationalError' in str(type(e)):
                generate_log("CRITICAL", "Connection refused ")
            else:
                return response(msg="Technical error", code=500)

    def __check_data(self, email, password):
        if not all((email, password)):
            return {"msg": 'Email, and Password are required', "code": 400, "flag": False}
        elif len(password) > 225 or len(email) > 225:
            return {"msg": "Email or Password cannot be too long", "code": 400, "flag": False}
        elif not Validation.is_valid_email(email):
            return {"msg": "Entered invalid email", "code": 400, "flag": False}
        else:
            return {"flag": True}

    @valid_jti_required
    def logout(self):
        current_user = get_jwt_identity()
        userJwtToken = UserJwtTokens()
        is_token_exists = userJwtToken.get_user(id=current_user)
        if is_token_exists:
            result = is_token_exists.delete_token()
            if result:
                return response(msg=f'logout successful', code=200)
        return response(msg=f'logout successful', code=400)
