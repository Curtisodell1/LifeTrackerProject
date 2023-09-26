from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db

# Models go here!


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String)
    activity_status = db.Column(db.String)


    serialize_rules = ('-days.activity',)
    

    @validates('activity_status')
    def validate_activity_status(self, db_column, activity_status):
        activity_status_values = ('Yes', 'No')
        if activity_status in activity_status_values:
            return activity_status
        else:
            raise ValueError("Activity Status must be Yes or No. ")

    


class Feeling(db.Model, SerializerMixin):
    __tablename__ = 'feelings'
    id = db.Column(db.Integer, primary_key=True)
    morning_feeling = db.Column(db.Integer)
    afternoon_feeling = db.Column(db.Integer)
    evening_feeling = db.Column(db.Integer)
    description = db.Column(db.String)

    serialize_rules = ('-days.feeling',)
    
    @validates('morning_feeling')
    def validate_feeling(self, db_column, morning_feeling):
        if type(morning_feeling) is int and 0 <= morning_feeling <= 10:
            return morning_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    @validates('afternoon_feeling')
    def validate_afternoon_feeling(self, db_column, afternoon_feeling):
        if type(afternoon_feeling) is int and 0 <= afternoon_feeling <= 10:
            return afternoon_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    
    @validates('evening_feeling')
    def validate_evening_feeling(self, db_column, evening_feeling):
        if type(evening_feeling) is int and 0 <= evening_feeling <= 10:
            return evening_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    
    @validates('description')
    def validate_description(self, db_column, description):
        if type(description) is str and 0 <= description <= 200:
            return description
        else:
            raise ValueError('Description must be a string of 0 to 200 characters long. ')

    
    
class Day(db.Model, SerializerMixin):
    __tablename__ = "days"
    # every day will have a feeling and activity
    id = db.Column(db.Integer, primary_key=True)
    feeling_id = db.Column(db.Integer, db.ForeignKey("feelings.id"))
    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"))


    serialize_rules = ('activities.days','-feeling.days')
    
    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    _password_hash = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    validation_errors = []


    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        from app import bcrypt
        if type(password) is str and len(password) in range ( 5, 16):
            password_has = bcrypt.generate_password_hash(password.encode('utf-8'))
            self._password_hash = password.decode('utf-8')
        else:
            self.validation_errors.append("Password must be 5 and 15 characters long. ")
    
        
    


