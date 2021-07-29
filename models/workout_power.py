from . import db
from sqlalchemy import ForeignKey
from .base_model import BaseModel


class WorkoutPowerModel(db.Model, BaseModel):
    __tablename__ = 'workout_power'
    workout_id = db.Column(db.Integer, ForeignKey('workout.workout_id', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    power_maximum = db.Column(db.Float)
    power_average = db.Column(db.Float)
    normalized_power = db.Column(db.Float)
    power_5_seconds = db.Column(db.Float)
    power_10_seconds = db.Column(db.Float)
    power_12_seconds = db.Column(db.Float)
    power_20_seconds = db.Column(db.Float)
    power_30_seconds = db.Column(db.Float)
    power_1_minute = db.Column(db.Float)
    power_2_minutes = db.Column(db.Float)
    power_5_minutes = db.Column(db.Float)
    power_6_minutes = db.Column(db.Float)
    power_10_minutes = db.Column(db.Float)
    power_12_minutes = db.Column(db.Float)
    power_20_minutes = db.Column(db.Float)
    power_30_minutes = db.Column(db.Float)
    power_1_hour = db.Column(db.Float)
    power_90_minutes = db.Column(db.Float)
    power_3_hours = db.Column(db.Float)
    power_zone_1 = db.Column(db.Float)
    power_zone_2 = db.Column(db.Float)
    power_zone_3 = db.Column(db.Float)
    power_zone_4 = db.Column(db.Float)
    power_zone_5 = db.Column(db.Float)
    power_zone_6 = db.Column(db.Float)
    power_zone_7 = db.Column(db.Float)
    power_zone_1_min = db.Column(db.Float)
    power_zone_2_min = db.Column(db.Float)
    power_zone_3_min = db.Column(db.Float)
    power_zone_4_min = db.Column(db.Float)
    power_zone_5_min = db.Column(db.Float)
    power_zone_6_min = db.Column(db.Float)
    power_zone_7_min = db.Column(db.Float)

    def __init__(self,  workout_id, power_5_seconds=None, power_10_seconds=None,
                 power_12_seconds=None, power_20_seconds=None, power_30_seconds=None, power_1_minute=None, power_2_minutes=None, power_5_minutes=None,
                 power_6_minutes=None, power_10_minutes=None, power_12_minutes=None, power_20_minutes=None, power_30_minutes=None, power_1_hour=None,
                 power_90_minutes=None, power_3_hours=None, power_timezones=None, power_maximum=None, power_average=None, normalized_power=None):
        self.power_maximum = power_maximum
        self.power_average = power_average
        self.normalized_power = normalized_power
        self.workout_id = workout_id
        self.power_5_seconds = power_5_seconds
        self.power_10_seconds = power_10_seconds
        self.power_12_seconds = power_12_seconds
        self.power_20_seconds = power_20_seconds
        self.power_30_seconds = power_30_seconds
        self.power_1_minute = power_1_minute
        self.power_2_minutes = power_2_minutes
        self.power_5_minutes = power_5_minutes
        self.power_6_minutes = power_6_minutes
        self.power_10_minutes = power_10_minutes
        self.power_12_minutes = power_12_minutes
        self.power_20_minutes = power_20_minutes
        self.power_30_minutes = power_30_minutes
        self.power_1_hour = power_1_hour
        self.power_90_minutes = power_90_minutes
        self.power_3_hours = power_3_hours
        if power_timezones is not None:
            self.power_zone_1 = None if "0" not in power_timezones else power_timezones["0"]["Seconds"]
            self.power_zone_2 = None if "1" not in power_timezones else power_timezones["1"]["Seconds"]
            self.power_zone_3 = None if "2" not in power_timezones else power_timezones["2"]["Seconds"]
            self.power_zone_4 = None if "3" not in power_timezones else power_timezones["3"]["Seconds"]
            self.power_zone_5 = None if "4" not in power_timezones else power_timezones["4"]["Seconds"]
            self.power_zone_6 = None if "5" not in power_timezones else power_timezones["5"]["Seconds"]
            self.power_zone_7 = None if "6" not in power_timezones else power_timezones["6"]["Seconds"]
            self.power_zone_1_min = None if "0" not in power_timezones else power_timezones["0"]["Minimum"]
            self.power_zone_2_min = None if "1" not in power_timezones else power_timezones["1"]["Minimum"]
            self.power_zone_3_min = None if "2" not in power_timezones else power_timezones["2"]["Minimum"]
            self.power_zone_4_min = None if "3" not in power_timezones else power_timezones["3"]["Minimum"]
            self.power_zone_5_min = None if "4" not in power_timezones else power_timezones["4"]["Minimum"]
            self.power_zone_6_min = None if "5" not in power_timezones else power_timezones["5"]["Minimum"]
            self.power_zone_7_min = None if "6" not in power_timezones else power_timezones["6"]["Minimum"]


