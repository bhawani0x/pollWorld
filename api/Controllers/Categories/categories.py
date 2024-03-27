from api.Models.Categories import Categories
from flask import Blueprint, request
from flask.views import View
from api.Helper.helper import response

category_bp = Blueprint('categories_bp', __name__)


class Category(View):

    def dispatch_request(self):
        if request.method == "GET":
            all_topics = Categories().all_topics()
            topic_dicts = [{"id": topic.id, "topic": topic.topic} for topic in all_topics]
            return response(msg=topic_dicts, code=200)
        elif request.method == "POST":
            return self.create_topic()

    def create_topic(self):
        data = request.get_json()
        topic = data.get('topic')
        topic_id = Categories().create(topic)
        return response(msg=str(topic_id.id), code=201)
