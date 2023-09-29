#!/usr/bin/env python3

# Standard library imports

# Remote library imports

from flask import Flask, request, session
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from flask import Flask, request, make_response
# Local imports

from config import app, db, api
# Add your model imports

from models import Entry, User

# Views go here!
validation_errors = {"errors":["validation errors"]}



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


    

class Entries(Resource):
    def get(self):
        entries = Entry.query.all()
        entries_dict = [entry.to_dict() for entry in entries]
        return make_response( entries_dict, 200 )
    
    def post(self):
        rq = request.get_json()
        try:
            new_entry = Entry(
                feeling = rq.get('feeling'),
                description = rq.get('description'),
                walk = rq.get('walk'),
                read = rq.get('read'),
                project = rq.get('project')
            )
            db.session.add(new_entry)
            db.session.commit()
            return make_response(new_entry.to_dict(), 201)
        except:
            return make_response(validation_errors, 400)
        
api.add_resource( Entries, '/entries')

class User(Resource):
    def get(self):
        entries = Entry.query.all()
        entries_dict = [entry.to_dict() for entry in entries]
        return make_response( entries_dict, 200 )
    
# class EntryById(Resource):
#     def get(self, id ):
#         entry = Entry.query.filter_by(id=id).first()
#         if 


if __name__ == '__main__':
    app.run(port=5555, debug=True)

