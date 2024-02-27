from flask import Blueprint, request
from flask.views import View
from api.Model.User import User, user_categories, db
from api.Helper.helper import response
from api.Model.Categories import Categories as CategoryModel

profileUpdate_bp = Blueprint("profileUpdate", __name__)


class ProfileUpdate(View):
    def dispatch_request(self):
        if request.method == "PUT":
            data = request.get_json()
            user_id = data.get('user_id')
            categories = data.get('categories')

            if user_id and categories:
                user = User.query.get(user_id)
                if user:
                    try:
                        # Clear existing categories
                        user.categories.clear()
                        # Add new categories
                        for category_id in categories:
                            user.categories.append(CategoryModel.query.get(category_id))

                        # Commit changes
                        db.session.commit()

                        return response("Profile updated successfully", 200)
                    except Exception as e:
                        db.session.rollback()
                        return response("Failed to update profile", 500)
                else:
                    return response("User not found", 404)
            else:
                return response("Invalid request data", 400)
        else:
            return response("Method not allowed", 405)
