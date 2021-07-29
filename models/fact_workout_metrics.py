from . import db
from .base_model import BaseModel


class FactWorkoutMetricsModel(db.Model, BaseModel):
    __bind_key__ = 'db2'
    __tablename__ = 'fact_workout_metrics'
    last_week_num = db.Column(db.Integer, primary_key=True)
    cyclist_id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    tss_actual = db.Column(db.Float)
    elevation_gain = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    temp_avg = db.Column(db.Float)
    rides_over_temp_28 = db.Column(db.Integer)

    def __init__(self, cyclist_id, last_week_num, distance, tss_actual, elevation_gain,
                 temp_min, temp_max, temp_avg, rides_over_temp_28):
        self.cyclist_id = cyclist_id
        self.last_week_num = last_week_num
        self.distance = distance
        self.elevation_gain = elevation_gain
        self.tss_actual = tss_actual
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.temp_avg = temp_avg
        self.rides_over_temp_28 = rides_over_temp_28
