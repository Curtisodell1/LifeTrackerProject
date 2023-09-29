from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!


class Entry(db.Model, SerializerMixin):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    feeling = db.Column(db.Integer)
    description = db.Column(db.String)
    walk = db.Column(db.Integer)
    read = db.Column(db.Integer)
    project = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    serialize_rules = ("-user.entries",)

    @validates('description')
    def validate_description(self, db_column, description):
        if type(description) is str and 0 <= len(description) <= 200:
            return description
        else:
            raise ValueError('Description must be a string of 0 to 200 characters long. ')
    # @validates('walk')
    # def validate_walk(self, db_column, read):
    #     if type(read) is int and read == 1:
    #         if read == 0 :
    #             return "No"
    #         return "Yes"
    #     else:
    #         raise ValueError('Must be a value of 0 or 1')    

    def __repr__(self):
        return f'<Feeling : {self.feeling}, Description : {self.description}>'
    

    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    # _password_hash = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    entries = db.relationship("Entry", backref = "user")



    # serialize_rules = ( '-_password_hash', )

    # validation_errors = []

    # # @classmethod
    # def clear_validation_errors(cls):
    #     cls.validation_errors = []

    # @hybrid_property
    # def password_hash(self):
    #     return self._password_hash

    # @password_hash.setter
    # def password_hash(self, password):
    #     from app import bcrypt
    #     if type(password) is str and len(password) in range(5, 16):
    #         self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')
    #     else:
    #         self.validation_errors.append("Password must be 5 to 15 characters long.")

    # def authenticate ( self, password ) :
    #     from app import bcrypt
    #     return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ) )
    
    # @validates( 'username' )
    # def validate_username ( self, key, username ) :
    #     if type( username ) is str and username :
    #         return username
    #     else :
    #         self.validation_errors.append( 'Username cannot be blank.' )

    def __repr__(self):
        return f'< username:{self.username}'
    


