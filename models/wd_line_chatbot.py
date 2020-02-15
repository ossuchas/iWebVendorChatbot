from db import db
from typing import List
from datetime import datetime


class WDPOStatusModel(db.Model):
    __tablename__ = "vw_wd_line_chatbot"

    LogId = db.Column(db.Integer, primary_key=True)
    Tran_Id = db.Column(db.Integer)
    POID = db.Column(db.String(50))
    ModifyDateDisplay = db.Column(db.String(200))
    ModifyDate = db.Column(db.DateTime)
    ModifyBy = db.Column(db.String(50))
    Doc_Status = db.Column(db.String(255))
    Doc_StatusId = db.Column(db.String(2))

    @classmethod
    def find_by_po(cls, _po_id: str) -> List["WDPOStatusModel"]:
        return cls.query.filter_by(POID=_po_id).order_by(cls.ModifyDate.desc()).all()

    @classmethod
    def find_by_tran_id(cls, _tran_id: str) -> List["WDPOStatusModel"]:
        return cls.query.filter_by(Tran_Id=_tran_id).order_by(cls.ModifyDate.desc()).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
