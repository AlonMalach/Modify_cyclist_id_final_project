from . import db
from .base_model import BaseModel


class FactWorkoutPowerModel(db.Model, BaseModel):
    __bind_key__ = 'db2'
    __tablename__ = 'fact_workout_power'
    last_week_num = db.Column(db.Integer, primary_key=True)
    cyclist_id = db.Column(db.Integer, primary_key=True)
    best_power_5_seconds = db.Column(db.Float)
    best_power_1_minute = db.Column(db.Float)
    best_power_5_minutes = db.Column(db.Float)
    best_power_20_minutes = db.Column(db.Float)

    def __init__(self, cyclist_id, last_week_num, best_power_5_seconds, best_power_1_minute, best_power_5_minutes, best_power_20_minutes):
        self.cyclist_id = cyclist_id
        self.last_week_num = last_week_num
        self.best_power_5_seconds = best_power_5_seconds
        self.best_power_1_minute = best_power_1_minute
        self.best_power_5_minutes = best_power_5_minutes
        self.best_power_20_minutes = best_power_20_minutes
