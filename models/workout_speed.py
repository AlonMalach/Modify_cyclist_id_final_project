from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class WorkoutSpeedModel(db.Model, BaseModel):
    __tablename__ = 'workout_speed'

    workout_id = db.Column(db.Integer, ForeignKey('workout.workout_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    speed_5_seconds = db.Column(db.Float)
    speed_10_seconds = db.Column(db.Float)
    speed_12_seconds = db.Column(db.Float)
    speed_20_seconds = db.Column(db.Float)
    speed_30_seconds = db.Column(db.Float)
    speed_1_minute = db.Column(db.Float)
    speed_2_minutes = db.Column(db.Float)
    speed_5_minutes = db.Column(db.Float)
    speed_6_minutes = db.Column(db.Float)
    speed_10_minutes = db.Column(db.Float)
    speed_12_minutes = db.Column(db.Float)
    speed_20_minutes = db.Column(db.Float)
    speed_30_minutes = db.Column(db.Float)
    speed_1_hour = db.Column(db.Float)
    speed_90_minutes = db.Column(db.Float)
    speed_3_hours = db.Column(db.Float)
    speed_zone_1 = db.Column(db.Float)
    speed_zone_2 = db.Column(db.Float)
    speed_zone_3 = db.Column(db.Float)
    speed_zone_4 = db.Column(db.Float)
    speed_zone_5 = db.Column(db.Float)
    speed_zone_6 = db.Column(db.Float)
    speed_zone_7 = db.Column(db.Float)
    speed_zone_1_min = db.Column(db.Float)
    speed_zone_2_min = db.Column(db.Float)
    speed_zone_3_min = db.Column(db.Float)
    speed_zone_4_min = db.Column(db.Float)
    speed_zone_5_min = db.Column(db.Float)
    speed_zone_6_min = db.Column(db.Float)
    speed_zone_7_min = db.Column(db.Float)

    def __init__(self, workout_id, speed_5_seconds=None, speed_10_seconds=None, speed_12_seconds=None, speed_20_seconds=None,
                 speed_30_seconds=None, speed_1_minute=None, speed_2_minutes=None, speed_5_minutes=None, speed_6_minutes=None,
                 speed_10_minutes=None,speed_12_minutes=None, speed_20_minutes=None, speed_30_minutes=None, speed_1_hour=None,
                 speed_90_minutes=None, speed_3_hours=None,speed_timezones=None):
        self.workout_id = workout_id
        self.speed_5_seconds = speed_5_seconds
        self.speed_10_seconds = speed_10_seconds
        self.speed_12_seconds = speed_12_seconds
        self.speed_20_seconds = speed_20_seconds
        self.speed_30_seconds = speed_30_seconds
        self.speed_1_minute = speed_1_minute
        self.speed_2_minutes = speed_2_minutes
        self.speed_5_minutes = speed_5_minutes
        self.speed_6_minutes = speed_6_minutes
        self.speed_10_minutes = speed_10_minutes
        self.speed_12_minutes = speed_12_minutes
        self.speed_20_minutes = speed_20_minutes
        self.speed_30_minutes = speed_30_minutes
        self.speed_1_hour = speed_1_hour
        self.speed_90_minutes = speed_90_minutes
        self.speed_3_hours = speed_3_hours
        if speed_timezones is not None:
            self.speed_zone_1 = None if "0" not in speed_timezones else speed_timezones["0"]["Seconds"]
            self.speed_zone_2 = None if "1" not in speed_timezones else speed_timezones["1"]["Seconds"]
            self.speed_zone_3 = None if "2" not in speed_timezones else speed_timezones["2"]["Seconds"]
            self.speed_zone_4 = None if "3" not in speed_timezones else speed_timezones["3"]["Seconds"]
            self.speed_zone_5 = None if "4" not in speed_timezones else speed_timezones["4"]["Seconds"]
            self.speed_zone_6 = None if "5" not in speed_timezones else speed_timezones["5"]["Seconds"]
            self.speed_zone_7 = None if "6" not in speed_timezones else speed_timezones["6"]["Seconds"]
            self.speed_zone_1_min = None if "0" not in speed_timezones else speed_timezones["0"]["Minimum"]
            self.speed_zone_2_min = None if "1" not in speed_timezones else speed_timezones["1"]["Minimum"]
            self.speed_zone_3_min = None if "2" not in speed_timezones else speed_timezones["2"]["Minimum"]
            self.speed_zone_4_min = None if "3" not in speed_timezones else speed_timezones["3"]["Minimum"]
            self.speed_zone_5_min = None if "4" not in speed_timezones else speed_timezones["4"]["Minimum"]
            self.speed_zone_6_min = None if "5" not in speed_timezones else speed_timezones["5"]["Minimum"]
            self.speed_zone_7_min = None if "6" not in speed_timezones else speed_timezones["6"]["Minimum"]

