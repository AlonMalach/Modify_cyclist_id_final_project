from sqlalchemy import exc

from . import db
from flask import current_app

# This class expends by all model classes.
class BaseModel:

    # This function used to save data into DB.
    def save_to_db(self):
        try:
            with current_app.app_context():
                db.session.add(self)
                db.session.commit()
                return self
        except exc.SQLAlchemyError as e:
            current_app.logger.error("Error on insert to DB" + str(e))
            print("base_model - Error on insert to DB" + str(e))
            return None

    # This function used to delete data from DB.
    def delete(self):
        try:
            with current_app.app_context():
                db.session.delete(self)
                db.session.commit()
        except exc.SQLAlchemyError:
            current_app.logger.error("Error on insert to DB" + str(exc))
            print("base_model - Error on delete from DB" + str(exc))