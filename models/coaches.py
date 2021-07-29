from . import db
from .base_model import BaseModel
from flask import current_app
from sqlalchemy import exc


class CoachModel(db.Model, BaseModel):
    __tablename__ = 'coaches'
    __table_args__ = (
        db.UniqueConstraint('full_name', name='unique_coach_constraint'),
    )
    coach_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    full_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    mobile = db.Column(db.String(80))

    def __init__(self, full_name, email, mobile):
        self.full_name = full_name
        self.email = email
        self.mobile = mobile

    def edit_coach(self, full_name, email, mobile):
        try:
            with current_app.app_context():
                self.mobile = mobile if mobile and len(mobile) != 0 else None
                self.email = email if len(email) != 0 else None
                self.full_name = full_name if len(full_name) != 0 else None
                db.session.commit()
        except exc.SQLAlchemyError:
            current_app.logger.error("Error on insert to DB" + str(exc))
            print("base_model - Error on insert to DB" + str(exc))

