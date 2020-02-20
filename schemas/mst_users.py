from ma import ma
from models.mst_users import UsersModel


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = UsersModel
