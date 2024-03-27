from flask import Blueprint, request
from flask.views import View
from api.Models.User import User
from api.Helper.helper import response
from api.Decorators.verify_user import valid_jti_required, get_jwt_identity

profileUpdate_bp = Blueprint("profileUpdate", __name__)


class ProfileUpdate(View):
    decorators = [valid_jti_required]

    def dispatch_request(self):
        if request.method == 'GET':
            return self.profile()
        elif request.method == "PUT":
            return self.update_profile()

    def profile(self):
        user = User().get_user_by_id(get_jwt_identity())
        categories = []
        for category in user.categories:
            categories.append(category.topic)
        return response({"user_data": {"name": user.name, "email": user.email, "username": user.username,
                                       "dob": user.dob, "gender": user.gender, "category": categories}}, 200)

    def update_profile(self):
        is_user_exists = User().get_user_by_id(get_jwt_identity())
        if is_user_exists:
            try:
                if request.get_json().get('category'):
                    categories = request.get_json().get('category')
                    if not User().update_categories(is_user_exists, categories):
                        return response("Profile not updated", 400)
                    # if not is_user_exists.update_profile():
                    #     return response("Profile not updated", 400)
                    return response("Profile updated", 200)
            except Exception as e:
                return response("Failed to update profile", 500)
        else:
            return response("User not found", 404)
