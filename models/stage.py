from sqlalchemy import ForeignKey
from . import db
from .base_model import BaseModel


class StageModel(db.Model, BaseModel):
    __tablename__ = 'stages'
    stage_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage_pcs_id = db.Column(db.Integer)
    race_pcs_id = db.Column(db.Integer)
    event_pcs_id = db.Column(db.Integer)
    edition_pcs_id = db.Column(db.Integer)
    race_name = db.Column(db.String(80))
    race_date = db.Column(db.Date)
    stage_date = db.Column(db.Date)
    stage_name = db.Column(db.String(80))
    stage_number = db.Column(db.Integer)
    stage_type = db.Column(db.Integer)
    classification = db.Column(db.String(10))
    nation = db.Column(db.String(20))
    pcs_link = db.Column(db.String(150))
    profile_score = db.Column(db.Integer)
    profile_score_final = db.Column(db.Integer)
    parcours_type = db.Column(db.Integer)
    parcours_type_name = db.Column(db.String(30))
    pcs_city_start = db.Column(db.String(80))
    pcs_city_finish = db.Column(db.String(80))
    is_stage_race = db.Column(db.Boolean)
    veloviewer_description = db.Column(db.String(80))
    veloviewer_type = db.Column(db.String(10))
    distance = db.Column(db.Float)
    elevation = db.Column(db.Float)
    VVOM = db.Column(db.Integer)
    _1000_to_1500_m = db.Column(db.Float)
    _1500_to_2000_m = db.Column(db.Float)
    _2000_to_2500_m = db.Column(db.Float)
    _2500_to_3000_m = db.Column(db.Float)
    _3000_to_3500_m = db.Column(db.Float)
    race_total_distance = db.Column(db.Float)
    race_total_elevation = db.Column(db.Float)
    race_total_VVOM = db.Column(db.Integer)

    def __init__(self, stage_pcs_id=None, race_pcs_id=None, event_pcs_id=None, edition_pcs_id=None, race_name=None,
                 race_date=None, stage_date=None, stage_name=None, stage_number=None, stage_type=None,
                 classification=None, nation=None,
                 profile_score=None, profile_score_final=None, parcours_type=None, parcours_type_name=None,
                 pcs_city_start=None, pcs_city_finish=None, is_stage_race=None, pcs_link=None,
                 veloviewer_description=None, veloviewer_type=None, distance=None, elevation=None, VVOM=None,
                 _1000_to_1500_m=None,
                 _1500_to_2000_m=None, _2000_to_2500_m=None, _2500_to_3000_m=None, _3000_to_3500_m=None,
                 race_total_distance=None, race_total_elevation=None, race_total_VVOM=None):
        self.stage_pcs_id = stage_pcs_id
        self.race_pcs_id = race_pcs_id
        self.event_pcs_id = event_pcs_id
        self.edition_pcs_id = edition_pcs_id
        self.race_name = race_name
        self.race_date = race_date
        self.stage_date = stage_date
        self.stage_name = stage_name
        self.stage_number = stage_number
        self.stage_type = stage_type
        self.classification = classification
        self.nation = nation
        self.pcs_link = pcs_link
        self.profile_score = profile_score
        self.profile_score_final = profile_score_final
        self.parcours_type = parcours_type
        self.parcours_type_name = parcours_type_name
        self.pcs_city_start = pcs_city_start
        self.pcs_city_finish = pcs_city_finish
        self.is_stage_race = is_stage_race
        self.veloviewer_description = veloviewer_description
        self.veloviewer_type = veloviewer_type
        self.distance = distance
        self.elevation = elevation
        self.VVOM = VVOM
        self._1000_to_1500_m = _1000_to_1500_m
        self._1500_to_2000_m = _1500_to_2000_m
        self._2000_to_2500_m = _2000_to_2500_m
        self._2500_to_3000_m = _2500_to_3000_m
        self._3000_to_3500_m = _3000_to_3500_m
        self.race_total_distance = race_total_distance
        self.race_total_elevation = race_total_elevation
        self.race_total_VVOM = race_total_VVOM

    def get_cyclist_id(self):
        return self.cyclist_id
