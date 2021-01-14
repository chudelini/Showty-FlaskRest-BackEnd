from ma import ma
from models.user import UserModel

class UserUpdateSchema(ma.SQLAlchemySchema):

    class Meta:
        model = UserModel
        load_only = ("password", "image_id", "image_width", "image_height", "activated")
        dump_only = ("activated",)
        exclude = ("password", "id", "email", "login")




class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = UserModel
        load_only = ("password", )
        dump_only = ("activated",)
        exclude = ("id",)

