from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class CyclistNrBySeasonModel(db.Model, BaseModel):
    __tablename__ = 'cyclists_nrs_by_seasons'

    cyclist_id = db.Column(db.Integer, ForeignKey('cyclists.cyclist_id', onupdate="CASCADE", ondelete="CASCADE"),
                           primary_key=True)
    season = db.Column(db.Integer, primary_key=True)
    nr_results = db.Column(db.Integer)

    def __init__(self, cyclist_id, season, nr_results=None):
        self.cyclist_id = cyclist_id
        self.season = season
        self.nr_results = nr_results

