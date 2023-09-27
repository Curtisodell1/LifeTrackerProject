#!/usr/bin/env python3

# Standard library imports

# Remote library imports

from flask import Flask, request, session
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS

# Local imports

from config import app, db, api
# Add your model imports

from models import Activity, User, Feeling, Day

# Views go here!




class Signup(Resource):
    def post(self):
        rq = request.get_json()
        User.clear_validation_errors()
        try:
            new_user = User(
                username = rq['username'],
                password_hash = rq['password']
            )
            if new_user.validation_errors:
                raise ValueError
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id

            return new_user.to_dict(), 201
        except:
            errors =  new_user.validation_errors
            new_user.clear_validation_errors()
            return {'errors':'errors'}, 422

api.add_resource(Signup, '/signup', endpoint = 'signup')


class Login(Resource):
    def post(self):
        username = request.get_json()[ 'username' ]
        password = request.get_json()[ 'password' ]

        user = User.query.filter( User.username.like( f'{ username }' ) ).first()

        if user and user.authenticate( password ) :
            session[ 'user_id' ] = user.id
            print( session[ 'user_id' ] )
            return user.to_dict(), 200
        else :
            return { 'errors':['Invalid username or password.'] }, 404

api.add_resource( Login, '/login', endpoint = 'login' )

class Logout ( Resource ) :
    def delete ( ) :
        session[ 'user_id' ] = None
        return {}, 204

class Activities(Resource):
    def get(self):
        return Activity.all(), 200
    
    

class Feelings(Resource):
    def get(self):
        return Feeling.all(), 200

    def post(self):
        rq = request.get_json
        try:
            new_feeling = Feeling(
                morning_feeling = rq['morning_feeling'],
                afternoon_feeling = rq['afternoon_feeling'],
                evening_feeling = rq['evening_feeling'],
                description = rq['description']
            )
            if new_feeling.validion_errors:
                raise ValueError
            db.session.add(new_feeling)
            db.session.commit()
            return new_feeling.to_dict(), 201
        except:
            errors = new_feeling.validation_errors
            new_feeling.clear_validation_errors()
            return {'errors': 'errors'}, 422
        
api.add_resource(Feelings, '/feelings')


class Days(Resource):
    def get(self):
        return Day.all(), 200

    def post(self):
        rq = request.get_json
        try:
            new_day = Day(
                
            )
            if new_day.validion_errors:
                raise ValueError
            db.session.add(new_day)
            db.session.commit()
            return new_day.to_dict(), 201
        except:
            errors = new_day.validation_errors
            new_day.clear_validation_errors()
            return {'errors': 'errors'}, 422



api.add_resource(Days, '/days')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

