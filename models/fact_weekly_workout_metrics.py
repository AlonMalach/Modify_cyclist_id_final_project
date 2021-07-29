from . import db
from .base_model import BaseModel


class FactWeeklyWorkoutMetricsModel(db.Model, BaseModel):
    __bind_key__ = 'db2'
    __tablename__ = 'fact_weekly_workout_metrics'
    last_week_num = db.Column(db.Integer, primary_key=True)
    cyclist_id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    tss_actual = db.Column(db.Float)
    elevation_gain = db.Column(db.Float)
    hours = db.Column(db.Float)
    power_5_seconds = db.Column(db.Float)
    power_10_seconds = db.Column(db.Float)
    power_20_seconds = db.Column(db.Float)
    power_30_seconds = db.Column(db.Float)
    power_1_minute = db.Column(db.Float)
    power_2_minutes = db.Column(db.Float)
    power_5_minutes = db.Column(db.Float)
    power_10_minutes = db.Column(db.Float)
    power_20_minutes = db.Column(db.Float)
    power_30_minutes = db.Column(db.Float)
    power_1_hour = db.Column(db.Float)
    power_3_hours = db.Column(db.Float)
    power_zone_3_min = db.Column(db.Float)
    power_zone_4_min = db.Column(db.Float)
    power_zone_5_min = db.Column(db.Float)
    power_zone_6_min = db.Column(db.Float)
    power_zone_7_min = db.Column(db.Float)

    def __init__(self, cyclist_id, last_week_num, distance, tss_actual, elevation_gain,
                 hours, power_5_seconds, power_10_seconds, power_20_seconds, power_30_seconds,
                 power_1_minute, power_2_minutes, power_5_minutes, power_10_minutes, power_20_minutes,
                 power_30_minutes, power_1_hour, power_3_hours, power_zone_3_min, power_zone_4_min,
                 power_zone_5_min, power_zone_6_min, power_zone_7_min):
        self.cyclist_id = cyclist_id
        self.last_week_num = last_week_num
        self.distance = distance
        self.elevation_gain = elevation_gain
        self.tss_actual = tss_actual
        self.hours = hours
        self.power_5_seconds = power_5_seconds
        self.power_10_seconds = power_10_seconds
        self.power_20_seconds = power_20_seconds
        self.power_30_seconds = power_30_seconds
        self.power_1_minute = power_1_minute
        self.power_2_minutes = power_2_minutes
        self.power_5_minutes = power_5_minutes
        self.power_10_minutes = power_10_minutes
        self.power_20_minutes = power_20_minutes
        self.power_30_minutes = power_30_minutes
        self.power_1_hour = power_1_hour
        self.power_3_hours = power_3_hours
        self.power_zone_3_min = power_zone_3_min
        self.power_zone_4_min = power_zone_4_min
        self.power_zone_5_min = power_zone_5_min
        self.power_zone_6_min = power_zone_6_min
        self.power_zone_7_min = power_zone_7_min
