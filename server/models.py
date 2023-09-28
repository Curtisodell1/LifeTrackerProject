from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!



class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String)
    activity_status = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-days.activity',)
    

    @validates('activity_status')
    def validate_activity_status(self, db_column, activity_status):
        activity_status_values = ('Yes', 'No')
        if activity_status in activity_status_values:
            return activity_status
        else:
            raise ValueError("Activity Status must be Yes or No. ")

    def __repr__(self):
        return f'<Activity:{self.activity}, Activity Status: {self.activity_status}'


class Feeling(db.Model, SerializerMixin):
    __tablename__ = 'feelings'
    id = db.Column(db.Integer, primary_key=True)
    morning_feeling = db.Column(db.Integer)
    afternoon_feeling = db.Column(db.Integer)
    evening_feeling = db.Column(db.Integer)
    description = db.Column(db.String)


    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ('-days.feeling',)
    
    @validates('morning_feeling')
    def validate_feeling(self, db_column, morning_feeling):
        if type(morning_feeling) is int and 0 < morning_feeling <= 10:
            return morning_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    @validates('afternoon_feeling')
    def validate_afternoon_feeling(self, db_column, afternoon_feeling):
        if type(afternoon_feeling) is int and 0 < afternoon_feeling <= 10:
            return afternoon_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    
    @validates('evening_feeling')
    def validate_evening_feeling(self, db_column, evening_feeling):
        if type(evening_feeling) is int and 0 < evening_feeling <= 10:
            return evening_feeling
        else:
            raise ValueError("Feeling has to be a number from 1 to 10")
    
    @validates('description')
    def validate_description(self, db_column, description):
        if type(description) is str and 0 <= len(description) <= 200:
            return description
        else:
            raise ValueError('Description must be a string of 0 to 200 characters long. ')

    def __repr__(self):
        return f'<Morning Feeling : {self.morning_feeling},Afternoon Feeling : {self.afternoon_feeling}, Evening Feeling : {self.evening_feeling}, Description : {self.description}'
    
    
class Day(db.Model, SerializerMixin):
    __tablename__ = "days"
    # every day will have a feeling and activity
    id = db.Column(db.Integer, primary_key=True)
    # average_day_feeling = db.Column(db.Integer)
    # daily_activity_point = db.Column(db.Integer)
    feeling_id = db.Column(db.Integer, db.ForeignKey("feelings.id"))
    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    # serialize_rules = ('activities.days','-feeling.days')
    
    def __repr__(self):
        return f'<Day : {self.id}'
    
    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    _password_hash = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    



    serialize_rules = ( '-_password_hash', )
    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    # def password_hash(self, password):
    #     from app import bcrypt
    #     if type(password) is str and len(password) in range ( 5, 16):
    #         password_has = bcrypt.generate_password_hash(password.encode('utf-8'))
    #         self._password_hash = password.decode('utf-8')
    #     else:
    #         self.validation_errors.append("Password must be 5 and 15 characters long. ")
    def password_hash(self, password):
        from app import bcrypt
        if type(password) is str and len(password) in range(5, 16):
            self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')
        else:
            self.validation_errors.append("Password must be 5 to 15 characters long.")

    def authenticate ( self, password ) :
        from app import bcrypt
        return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ) )
    
    @validates( 'username' )
    def validate_username ( self, key, username ) :
        if type( username ) is str and username :
            return username
        else :
            self.validation_errors.append( 'Username cannot be blank.' )

    def __repr__(self):
        return f'< username:{self.name}'
    


