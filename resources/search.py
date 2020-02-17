
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import UserModel
from schemas.user import UserSchema
from models.hashtag import HashtagModel




class Search(Resource):

    @jwt_required
    def get(self, keyword):
        login = get_jwt_identity()
        user = UserModel.find_by_username(login)
        if user:
            return [ {"search_result" : x.login } for x in UserModel.search_by_username(keyword)] + \
                   [ {"search_result" : "#" + x.hashtag } for x in HashtagModel.search_by_hashtag(keyword)], 200
        else:
            return {"message": "User not found"}, 404