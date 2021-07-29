from sqlalchemy import exc, ForeignKey
from . import db
from flask import current_app
from .base_model import BaseModel
from unidecode import unidecode
from sqlalchemy.ext.hybrid import hybrid_property


class CyclistModel(db.Model, BaseModel):
    __tablename__ = 'cyclists'
    __table_args__ = (
         db.UniqueConstraint('last_name', 'email', name='unique_cyclist_constraint'),
     )
    cyclist_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    pcs_id = db.Column(db.Integer)
    uci_id = db.Column(db.BigInteger)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birthdate = db.Column(db.Date)
    height = db.Column(db.Integer)
    pcs_weight = db.Column(db.Integer)
    birthplace = db.Column(db.String(80))
    rw = db.Column(db.Float)
    tp_id = db.Column(db.Integer)
    nation = db.Column(db.String(80))
    age = db.Column(db.Integer)
    pcs = db.Column(db.String(80))
    cyclist_class = db.Column(db.String(10))
    description = db.Column(db.String(80))
    email = db.Column(db.String(80))
    mobile = db.Column(db.String(80))
    coach_id = db.Column(db.Integer) #, ForeignKey('coaches.coach_id', onupdate="CASCADE", ondelete="CASCADE"))
    years_in_team = db.Column(db.Integer)
    url = db.Column(db.String(80))
    label = db.Column(db.String(80))
    team_label = db.Column(db.String(20))
    tp_weight = db.Column(db.Float)

    def __init__(self, first_name, last_name, tp_id, email, coach_id, label, team_label, rw=None, nation=None, age=None, pcs=None,
              cyclist_class=None,description=None, mobile=None, years_in_team=None, url=None,
              birthdate=None, birthplace=None, height=None, pcs_id=None, uci_id=None, pcs_weight=None, tp_weight=None):
         self.rw = rw
         self.tp_id = tp_id
         self.nation = nation
         self.age = age
         self.pcs = pcs
         self.cyclist_class = cyclist_class
         self.description = description
         self.email = email
         self.mobile = mobile
         self.coach_id = coach_id
         self.years_in_team = years_in_team
         self.url = url
         self.label = label
         self.team_label = team_label
         self.first_name = first_name
         self.last_name = last_name
         self.birthdate = birthdate
         self.birthplace = birthplace
         self.height = height
         self.pcs_id = pcs_id
         self.uci_id = uci_id
         self.pcs_weight = pcs_weight
         self.tp_weight = tp_weight

    def get_cyclist_id(self):
         return self.cyclist_id