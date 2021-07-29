from . import db
from sqlalchemy import exc
from flask import current_app, g
from werkzeug.security import generate_password_hash, check_password_hash
from .base_model import BaseModel
# from src.server import *
from os import environ
import jwt
import time

JWT_ALGORITHM = 'HS256'

class UserModel(db.Model, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    role = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)

    def __init__(self, username, email, created_on, role):
        self.username = username
        self.email = email
        self.created_on = created_on
        self.role = role

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expires_in=3600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            environ.get('SECRET_KEY'),
            algorithm=JWT_ALGORITHM
        )

    def get_roles(self):
        return self.role

    @staticmethod
    def verify_auth_token(token):
        try:
            token_content = jwt.decode(token,
                                       environ.get('SECRET_KEY'),
                                       algorithms=[JWT_ALGORITHM]
                                       )
        except jwt.exceptions.ExpiredSignatureError:
            current_app.logger.error("Access denied")
        except:
            return None  # In case it is an invalid token it can be an email

        return UserModel.query.get(token_content['id'])


    def edit_user(self, username, email, role):
        try:
            with current_app.app_context():
                self.username = username
                self. email = email
                self.role = role
                db.session.commit()
        except exc.SQLAlchemyError:
            current_app.logger.error("Error on insert to DB" + str(exc))
            print("base_model - Error on insert to DB" + str(exc))

# @auth.verify_password
def verify_password(email_or_token, password):
    user = UserModel.verify_auth_token(email_or_token)
    if not user:
        user = UserModel.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

# @auth.get_user_roles
def get_user_roles(user):
    current_user = UserModel.verify_auth_token(user['username'])
    return current_user.get_roles()