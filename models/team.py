from . import db
from .base_model import BaseModel
from sqlalchemy import ForeignKey, and_, func


class TeamModel(db.Model, BaseModel):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    team_pcs_id = db.Column(db.Integer)
    team_name = db.Column(db.String(80))
    season = db.Column(db.Integer)

    def __init__(self, team_name, team_pcs_id=None, season=None):
        self.team_name = team_name
        self.team_pcs_id = team_pcs_id
        self.season = season
