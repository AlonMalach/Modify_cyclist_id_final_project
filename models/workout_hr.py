from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class WorkoutHRModel(db.Model, BaseModel):
    __tablename__ = 'workout_hr'
    workout_id = db.Column(db.Integer, ForeignKey('workout.workout_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    hr_5_seconds = db.Column(db.Integer)
    hr_10_seconds = db.Column(db.Integer)
    hr_12_seconds = db.Column(db.Integer)
    hr_20_seconds = db.Column(db.Integer)
    hr_30_seconds = db.Column(db.Integer)
    hr_1_minute = db.Column(db.Integer)
    hr_2_minutes = db.Column(db.Integer)
    hr_5_minutes = db.Column(db.Integer)
    hr_6_minutes = db.Column(db.Integer)
    hr_10_minutes = db.Column(db.Integer)
    hr_12_minutes = db.Column(db.Integer)
    hr_20_minutes = db.Column(db.Integer)
    hr_30_minutes = db.Column(db.Integer)
    hr_1_hour = db.Column(db.Integer)
    hr_90_minutes = db.Column(db.Integer)
    hr_3_hours = db.Column(db.Integer)
    hr_zone_1 = db.Column(db.Float)
    hr_zone_2 = db.Column(db.Float)
    hr_zone_3 = db.Column(db.Float)
    hr_zone_4 = db.Column(db.Float)
    hr_zone_5 = db.Column(db.Float)
    hr_zone_1_Min = db.Column(db.Integer)
    hr_zone_2_Min = db.Column(db.Integer)
    hr_zone_3_Min = db.Column(db.Integer)
    hr_zone_4_Min = db.Column(db.Integer)
    hr_zone_5_Min = db.Column(db.Integer)


    def __init__(self, workout_id, hr_5_seconds=None, hr_10_seconds=None, hr_12_seconds=None, hr_20_seconds=None, hr_30_seconds=None,
                 hr_1_minute=None, hr_2_minutes=None,hr_5_minutes=None, hr_6_minutes=None, hr_10_minutes=None, hr_12_minutes=None,
                 hr_20_minutes=None, hr_30_minutes=None, hr_1_hour=None, hr_90_minutes=None, hr_3_hours=None, hr_timezones=None):
        self.workout_id = workout_id
        self.hr_5_seconds = hr_5_seconds
        self.hr_10_seconds = hr_10_seconds
        self.hr_12_seconds = hr_12_seconds
        self.hr_20_seconds = hr_20_seconds
        self.hr_30_seconds = hr_30_seconds
        self.hr_1_minute = hr_1_minute
        self.hr_2_minutes = hr_2_minutes
        self.hr_5_minutes = hr_5_minutes
        self.hr_6_minutes = hr_6_minutes
        self.hr_10_minutes = hr_10_minutes
        self.hr_12_minutes = hr_12_minutes
        self.hr_20_minutes = hr_20_minutes
        self.hr_30_minutes = hr_30_minutes
        self.hr_1_hour = hr_1_hour
        self.hr_90_minutes = hr_90_minutes
        self.hr_3_hours = hr_3_hours
        if hr_timezones is not None:
            self.hr_zone_1 = None if "0" not in hr_timezones else hr_timezones["0"]["Seconds"]
            self.hr_zone_2 = None if "1" not in hr_timezones else hr_timezones["1"]["Seconds"]
            self.hr_zone_3 = None if "2" not in hr_timezones else hr_timezones["2"]["Seconds"]
            self.hr_zone_4 = None if "3" not in hr_timezones else hr_timezones["3"]["Seconds"]
            self.hr_zone_5 = None if "4" not in hr_timezones else hr_timezones["4"]["Seconds"]
            self.hr_zone_1_Min = None if "0" not in hr_timezones else hr_timezones["0"]["Minimum"]
            self.hr_zone_2_Min = None if "1" not in hr_timezones else hr_timezones["1"]["Minimum"]
            self.hr_zone_3_Min = None if "2" not in hr_timezones else hr_timezones["2"]["Minimum"]
            self.hr_zone_4_Min = None if "3" not in hr_timezones else hr_timezones["3"]["Minimum"]
            self.hr_zone_5_Min = None if "4" not in hr_timezones else hr_timezones["4"]["Minimum"]

