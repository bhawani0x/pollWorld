import datetime
from api.connection import mongo


class Posts:
    @staticmethod
    def all_posts():
        posts_collection = mongo.db.posts
        return list(posts_collection.find({}))

    @staticmethod
    def create_post(user_id, question, options=None, answer=None):
        options = options or []
        created_at = datetime.datetime.utcnow()
        updated_at = datetime.datetime.utcnow()
        post_id = mongo.db.posts.insert_one({
            'user_id': user_id,
            'question': question,
            'options': options,
            'answer': answer,
            'created_at': created_at,
            'updated_at': updated_at
        })
        return str(post_id.inserted_id)

    @staticmethod
    def read_post(post_id):
        posts_collection = mongo.db.posts
        return posts_collection.find_one({'_id': ObjectId(post_id)})

    @staticmethod
    def update_post(post_id, question=None, options=None):
        update_data = {'updated_at': datetime.datetime.utcnow()}
        if question:
            update_data['question'] = question
        if options:
            update_data['options'] = options
        mongo.db.posts.update_one({'_id': ObjectId(post_id)}, {'$set': update_data})
        return Posts.read_post(post_id)

    @staticmethod
    def delete_post(post_id):
        result = mongo.db.posts.delete_one({'_id': ObjectId(post_id)})
        return result.deleted_count
