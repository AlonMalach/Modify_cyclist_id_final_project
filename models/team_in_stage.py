from sqlalchemy import ForeignKey
from . import db
from .base_model import BaseModel


class TeamInStageModel(db.Model, BaseModel):
    __tablename__ = 'teams_in_stages'
    stage_id = db.Column(db.Integer, ForeignKey('stages.stage_id', onupdate="CASCADE", ondelete="CASCADE"),
                         primary_key=True)
    team_id = db.Column(db.Integer, ForeignKey('teams.team_id', onupdate="CASCADE", ondelete="CASCADE"),
                        primary_key=True)

    def _init_(self, stage_id, team_id):
        self.stage_id = stage_id
        self.team_id = team_id
