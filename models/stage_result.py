from sqlalchemy import ForeignKey
from . import db
from .base_model import BaseModel


class StageResultModel(db.Model, BaseModel):
    __tablename__ = 'stages_results'
    stage_id = db.Column(db.Integer, ForeignKey('stages.stage_id', onupdate="CASCADE", ondelete="CASCADE"),
                         primary_key=True)
    limit_results = db.Column(db.Integer)
    result_time = db.Column(db.DateTime)
    exp_finish_time = db.Column(db.DateTime)
    finish_time = db.Column(db.DateTime)

    def __init__(self, stage_id,
                 limit_results=None, result_time=None, exp_finish_time=None, finish_time=None):
        self.stage_id = stage_id
        self.limit_results = limit_results
        self.result_time = result_time
        self.exp_finish_time = exp_finish_time
        self.finish_time = finish_time
