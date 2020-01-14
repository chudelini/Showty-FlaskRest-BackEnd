from db import db


class LikeModel(db.Model):

    __tablename__ = 'likes'

    likes_id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(80))

        
    @classmethod
    def find_by_post_id(cls, post_id):
        all_likes= cls.query.filter_by(post_id=post_id)
        return all_likes
    
    @classmethod
    def find_by_user_id(cls, user_id, post_id):
        all_likes= cls.query.filter_by(user_id=user_id, post_id=post_id).first()
        return all_likes

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

