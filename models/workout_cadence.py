from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class WorkoutCadenceModel(db.Model, BaseModel):
    __tablename__ = 'workout_cadence'
    workout_id = db.Column(db.Integer, ForeignKey('workout.workout_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    cadence_5_seconds = db.Column(db.Integer)
    cadence_10_seconds = db.Column(db.Integer)
    cadence_12_seconds = db.Column(db.Integer)
    cadence_20_seconds = db.Column(db.Integer)
    cadence_30_seconds = db.Column(db.Integer)
    cadence_1_minute = db.Column(db.Integer)
    cadence_2_minutes = db.Column(db.Integer)
    cadence_5_minutes = db.Column(db.Integer)
    cadence_6_minutes = db.Column(db.Integer)
    cadence_10_minutes = db.Column(db.Integer)
    cadence_12_minutes = db.Column(db.Integer)
    cadence_20_minutes = db.Column(db.Integer)
    cadence_30_minutes = db.Column(db.Integer)
    cadence_1_hour = db.Column(db.Integer)
    cadence_90_minutes = db.Column(db.Integer)
    cadence_3_hours = db.Column(db.Integer)


    def __init__(self, workout_id, cadence_5_seconds, cadence_10_seconds, cadence_12_seconds, cadence_20_seconds,
                 cadence_30_seconds,cadence_1_minute, cadence_2_minutes, cadence_5_minutes, cadence_6_minutes, cadence_10_minutes,
                 cadence_12_minutes, cadence_20_minutes, cadence_30_minutes, cadence_1_hour, cadence_90_minutes,
                 cadence_3_hours):
        self.workout_id = workout_id
        self.cadence_5_seconds = cadence_5_seconds
        self.cadence_10_seconds = cadence_10_seconds
        self.cadence_12_seconds = cadence_12_seconds
        self.cadence_20_seconds = cadence_20_seconds
        self.cadence_30_seconds = cadence_30_seconds
        self.cadence_1_minute = cadence_1_minute
        self.cadence_2_minutes = cadence_2_minutes
        self.cadence_5_minutes = cadence_5_minutes
        self.cadence_6_minutes = cadence_6_minutes
        self.cadence_10_minutes = cadence_10_minutes
        self.cadence_12_minutes = cadence_12_minutes
        self.cadence_20_minutes = cadence_20_minutes
        self.cadence_30_minutes = cadence_30_minutes
        self.cadence_1_hour = cadence_1_hour
        self.cadence_90_minutes = cadence_90_minutes
        self.cadence_3_hours = cadence_3_hours

