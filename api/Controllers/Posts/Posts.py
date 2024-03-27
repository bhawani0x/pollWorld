from api.Models.Posts import Posts
from flask import Blueprint, request
from flask.views import View
from api.Helper.helper import response
from api.Decorators.verify_user import valid_jti_required, get_jwt_identity
from bson import ObjectId


posts_bp = Blueprint('posts_bp', __name__)


class Post(View):

    def dispatch_request(self):
        if request.method == "GET":
            all_posts = Posts().all_posts()
            all_posts_list = []
            for post in all_posts:
                post['_id'] = str(post['_id'])
                all_posts_list.append(post)
            return response(msg=all_posts_list, code=200)
        elif request.method == "POST":
            return self.create_topic()

    @valid_jti_required
    def create_topic(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        question = data.get('question')
        options = data.get('options')
        post_id = Posts.create_post(user_id, question, options)
        return response(msg={'message': 'Post created', 'post_id': post_id}, code=201)
