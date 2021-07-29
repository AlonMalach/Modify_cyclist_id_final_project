from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class CyclistStatsModel(db.Model, BaseModel):
    __tablename__ = 'cyclists_stats'

    cyclist_id = db.Column(db.Integer, ForeignKey('cyclists.cyclist_id', onupdate="CASCADE", ondelete="CASCADE"),
                           primary_key=True)
    last_update = db.Column(db.DateTime, primary_key=True)
    gc = db.Column(db.Integer)
    itt = db.Column(db.Integer)
    sprint = db.Column(db.Integer)
    classic = db.Column(db.Integer)
    climber = db.Column(db.Integer)
    nr_wins = db.Column(db.Integer)
    nr_grandtours = db.Column(db.Integer)
    nr_classics = db.Column(db.Integer)

    def __init__(self, cyclist_id, last_update, gc=None, itt=None, sprint=None, classic=None, climber=None, nr_wins=None,
                 nr_grandtours=None, nr_classics=None):
        self.cyclist_id = cyclist_id
        self.last_update = last_update
        self.gc = gc
        self.itt = itt
        self.sprint = sprint
        self.classic = classic
        self.climber = climber
        self.nr_wins = nr_wins
        self.nr_grandtours = nr_grandtours
        self.nr_classics = nr_classics