#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Entry,User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        # Seed code goes here!
        Entry.query.delete()
        User.query.delete()
        print('tables cleared')

        u1 = User(username = 'Hiroki')
        u2 = User(username = 'Curtis')
        u3 = User(username = 'BreElle')
        u4 = User(username = 'Farhan')
        
        users = [u1,u2,u3,u4]

        db.session.add_all(users)
        db.session.commit()

        e1 = Entry(feeling = 1, description = "not going well", walk = 1, read = 1, project = 1, user_id = 1 )
        e2 = Entry(feeling = 4, description = "going well", walk = 0, read = 0, project = 1,user_id = 2  )
        e3 = Entry(feeling = 5, description = "well", walk = 0, read = 1, project = 1,user_id = 2  )
        e4 = Entry(feeling = 6, description = "not", walk = 1, read = 0, project = 1,user_id = 3 )

        entries = [e1, e2, e3, e4]
        db.session.add_all(entries)
        db.session.commit()

