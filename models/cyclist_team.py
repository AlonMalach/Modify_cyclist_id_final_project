from sqlalchemy import ForeignKey
from . import db
from .base_model import BaseModel


class CyclistTeamModel(db.Model, BaseModel):
    __tablename__ = 'cyclists_teams'
    cyclist_id = db.Column(db.Integer, ForeignKey('cyclists.cyclist_id', onupdate="CASCADE", ondelete="CASCADE"),
                           primary_key=True)
    season = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, ForeignKey('teams.team_id', onupdate="CASCADE", ondelete="CASCADE"),
                        primary_key=True)
    cyclist_class = db.Column(db.String(10), primary_key=True)
    cyclist_status = db.Column(db.String(10), primary_key=True)
    start_date = db.Column(db.Date)
    stop_date = db.Column(db.Date)

    def _init_(self, cyclist_id, season, team_id, cyclist_class, cyclist_status, start_date=None, stop_date=None):
        self.cyclist_id = cyclist_id
        self.season = season
        self.team_id = team_id
        self.cyclist_class = cyclist_class
        self.cyclist_status = cyclist_status
        self.start_date = start_date
        self.stop_date = stop_date
