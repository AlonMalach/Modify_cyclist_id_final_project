from sqlalchemy import ForeignKey
from . import db
from .base_model import BaseModel


class TeamStageResultModel(db.Model, BaseModel):
    __tablename__ = 'teams_stages_results'
    stage_id = db.Column(db.Integer, ForeignKey('stages.stage_id', onupdate="CASCADE", ondelete="CASCADE"),
                         primary_key=True)
    team_id = db.Column(db.Integer, ForeignKey('teams.team_id', onupdate="CASCADE", ondelete="CASCADE"),
                        primary_key=True)
    team_rank = db.Column(db.String(10))
    uci_points = db.Column(db.Integer)
    finish_time = db.Column(
        db.String(10))  # DNF=Did not finish / DNS=Did not start / OTL = Outside time limit / DF=Did finish, no result
    time_gap = db.Column(db.String(10))

    def __init__(self, stage_id, team_id, team_rank=None, uci_points=None, finish_time=None,
                 time_gap=None):
        self.stage_id = stage_id
        self.team_id = team_id
        self.team_rank = team_rank
        self.uci_points = uci_points
        self.finish_time = finish_time
        self.time_gap = time_gap
