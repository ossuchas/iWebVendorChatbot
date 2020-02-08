from db import db
from typing import List
from datetime import datetime, timedelta, date
from sqlalchemy import func, cast, DATE


class LogChatBotModel(db.Model):
    __tablename__ = "log_linechatbot"

    logid = db.Column(db.Integer, primary_key=True)
    replyToken = db.Column(db.String(255))
    source_groupId = db.Column(db.String(255))
    source_userId = db.Column(db.String(255))
    source_type = db.Column(db.String(50))
    timestamps = db.Column(db.String(100))
    message_type = db.Column(db.String(50))
    message_text = db.Column(db.String(4000))
    stickerId = db.Column(db.String(10))
    packageId = db.Column(db.String(5))

    beacon_hwid = db.Column(db.String(20))
    beacon_dm = db.Column(db.String(1000))
    beacon_type = db.Column(db.String(50))
    beacon_entrydate = db.Column(db.DateTime)

    register_flag = db.Column(db.String(2), default='N')
    register_empid = db.Column(db.String(50))
    register_email = db.Column(db.String(50))

    # createby = db.Column(db.String(50), default='autobot')
    # createdate = db.Column(db.DateTime, default=datetime.now())
    # modifyby = db.Column(db.String(50), default='autobot')
    # modifydate = db.Column(db.DateTime, default=datetime.now())

    @classmethod
    def find_by_id(cls, _logid: int) -> "LogChatBotModel":
        return cls.query.filter_by(logid=_logid).first()

    @classmethod
    def find_by_token_beacon_today(cls, _user_id: str) -> "LogChatBotModel":
        return cls.query.filter((cls.source_userId == _user_id),
                                (cls.message_type == 'beacon'),
                                (cast(cls.beacon_entrydate, DATE) == date.today())).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
