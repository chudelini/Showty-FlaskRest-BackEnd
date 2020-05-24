from flask_restful import Resource
from models.message import MessageModel
from schemas.message import MessageSchema


message_schema = MessageSchema()


class Messages(Resource):

    def get(self, loginA, loginB):

        return {'text_messages': [message_schema.dump(x) for x in MessageModel.find_by_pair(loginA, loginB)]}