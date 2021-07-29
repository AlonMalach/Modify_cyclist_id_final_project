from sqlalchemy.orm import declarative_base

from . import db
Base2 = declarative_base()


class MaorCyclist(Base2):
    __tablename__ = 'cyclists'
    __table_args__ = (
        db.UniqueConstraint('last_name', 'first_name', name='unique_cyclist_constraint'),
    )
    cyclist_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
