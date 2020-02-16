from db import db
from typing import List
from datetime import datetime


class POHeaderModel(db.Model):
    __tablename__ = "poheader"

    poid = db.Column(db.String(50), primary_key=True)
    vendorid = db.Column(db.String(50))
    vendorname = db.Column(db.String(200))

    @classmethod
    def find_by_poid(cls, _po_id: str) -> "POHeaderModel":
        return cls.query.filter_by(poid=_po_id).first()

    @classmethod
    def find_by_poid_by_vendor(cls, _po_id: str, _vendor_id: str) -> "POHeaderModel":
        return cls.query.filter_by(poid=_po_id, vendorid=_vendor_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
