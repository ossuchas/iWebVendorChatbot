from db import db
from typing import List
from datetime import datetime


class WDPOAllStatusModel(db.Model):
    __tablename__ = "vw_wd_all_line_chatbot"

    tran_id = db.Column(db.Integer, primary_key=True)
    poid = db.Column(db.String(50))
    CreateDateDisplay = db.Column(db.String(200))
    CreateDate = db.Column(db.DateTime)
    Doc_Status = db.Column(db.String(255))
    Doc_StatusId = db.Column(db.String(2))

    @classmethod
    def find_by_po(cls, _po_id: str) -> List["WDPOAllStatusModel"]:
        return cls.query.filter_by(poid=_po_id).order_by(cls.CreateDate.desc()).all()

    @classmethod
    def find_by_po_by_vendor(cls, _po_id: str, _vendor_id: str) -> "WDPOAllStatusModel":
        return cls.query.filter_by(poid=_po_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
