from db import db


class UsersModel(db.Model):
    __tablename__ = "Users"

    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50))
    FirstName = db.Column(db.String(500))
    LastName = db.Column(db.String(500))
    Password = db.Column(db.String(500))
    VendorCode = db.Column(db.String(50))
    UserType = db.Column(db.Integer)
    Email = db.Column(db.String(100))

    @classmethod
    def check_user_pass(cls, _username: str, _password: str) -> "UsersModel":
        return cls.query.filter_by(UserName=_username, Password=_password).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
