from . import db
from .base_model import BaseModel
from sqlalchemy import ForeignKey


class WorkoutModel(db.Model, BaseModel):
    __tablename__ = 'workout'
    __table_args__ = (
        db.UniqueConstraint('workout_tp_id', 'cyclist_id', name='unique_workout_constraint'),
    )
    workout_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    workout_tp_id = db.Column(db.Integer)
    cyclist_id = db.Column(db.Integer, ForeignKey('cyclists.cyclist_id', onupdate="CASCADE", ondelete="CASCADE"))
    type = db.Column(db.String(10))
    tags = db.Column(db.String(50))
    workout_date = db.Column(db.Date)
    workout_week = db.Column(db.Integer)
    workout_month = db.Column(db.Integer)
    workout_title = db.Column(db.String(80))
    cyclist_mass = db.Column(db.Float)
    elevation_gain = db.Column(db.Float)
    elevation_loss = db.Column(db.Float)
    elevation_average = db.Column(db.Float)
    elevation_maximum = db.Column(db.Float)
    elevation_minimum = db.Column(db.Float)
    temp_avg = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    total_time = db.Column(db.Float)
    distance = db.Column(db.Float)
    energy = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    IF = db.Column(db.Float)
    tss_actual = db.Column(db.Float)
    tss_calculation_method = db.Column(db.String(10))
    hidden = db.Column(db.Boolean)  # Not used
    locked = db.Column(db.Boolean)  # Not used


    def __init__(self, cyclist_id, type, workout_date, workout_week, workout_month, workout_title,
                 elevation_gain=None,
                 elevation_loss=None, elevation_average=None, elevation_maximum=None, elevation_minimum=None,
                 temp_avg=None, temp_min=None,
                 temp_max=None, total_time=None, distance=None, calories=None, IF=None,
                 tss_actual=None, tss_calculation_method=None, hidden=None, locked=None, workout_tp_id=None,
                 energy=None, cyclist_mass=None, tags=None):
        self.cyclist_id = cyclist_id
        self.type = type
        self.workout_date = workout_date
        self.workout_week = workout_week
        self.workout_month = workout_month
        self.workout_title = workout_title
        self.elevation_gain = elevation_gain
        self.elevation_loss = elevation_loss
        self.elevation_average = elevation_average
        self.elevation_maximum = elevation_maximum
        self.elevation_minimum = elevation_minimum
        self.temp_avg = temp_avg
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.total_time = total_time
        self.distance = distance
        self.calories = calories
        self.IF = IF
        self.tss_actual = tss_actual
        self.tss_calculation_method = tss_calculation_method
        self.hidden = hidden
        self.locked = locked
        self.workout_tp_id = workout_tp_id
        self.energy = energy
        self.cyclist_mass = cyclist_mass
        self.tags = tags
