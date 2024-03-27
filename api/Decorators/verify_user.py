from functools import wraps

from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity

from api.Helper.helper import response
from api.Models.UserJwtToken import UserJwtTokens


def valid_jti_required(fn):
    @wraps(fn)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        jti_token = get_jwt()['jti']
        is_valid = UserJwtTokens().get_user_by_token(token=jti_token)
        if is_valid['flag']:
            return fn(*args, **kwargs)
        else:
            return response(msg=is_valid["msg"], code=403)
    return decorated_function
