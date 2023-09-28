#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Activity, Feeling, User, Day

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        # Seed code goes here!
        Activity.query.delete()
        Feeling.query.delete()
        Day.query.delete()
        User.query.delete()
        db.session.commit()
        print('tables cleared')

        print ( "Creating Activity..." )

        activities = []
        a1 = Activity( activity = "Taking a walk", activity_status = "Yes")
        activities.append(a1)
        a2 = Activity( activity = "Taking a shower", activity_status = "Yes")
        activities.append(a2)
        a3 = Activity( activity = "Going to the gym/ Working out", 
        activity_status = "No")
        activities.append(a3)
        a4 = Activity( activity = "Cleaning your home", activity_status = "No")
        activities.append(a4)
        a5 = Activity( activity = "Reading a book", activity_status = "Yes")
        activities.append(a5)
        db.session.add_all(activities)
        db.session.commit()


        print ( "Writing out feelings... " )

        feelings = []
        f1 = Feeling( morning_feeling = 3, afternoon_feeling = 6, evening_feeling = 3, description = 'The day started off awful and ended that way. ')
        feelings.append(f1)
        f2 = Feeling( morning_feeling = 6, afternoon_feeling = 6, evening_feeling = 9, description = 'An ok start to the day with a great end. ')
        feelings.append(f2)
        f3 = Feeling( morning_feeling = 1, afternoon_feeling = 6, evening_feeling = 8, description = 'I thought it would be an awful day but turned out to be great.')
        feelings.append(f3)
        f4 = Feeling( morning_feeling = 10, afternoon_feeling = 6, evening_feeling = 3, description = 'Started off so well but just kept dropping. ')
        feelings.append(f4)
        f5 = Feeling( morning_feeling = 7, afternoon_feeling = 6, evening_feeling = 8, description = 'Just a good day.')
        feelings.append(f5)

        db.session.add_all(feelings)
        db.session.commit()

        users = []

        days = []
        d1 = Day(feeling_id = f1.id, activity_id = a1.id)
        days.append(d1)
        d2 = Day(feeling_id = f2.id, activity_id = a2.id)
        days.append(d2)
        d3 = Day(feeling_id = f3.id, activity_id = a3.id)
        days.append(d3)
        d4 = Day(feeling_id = f4.id, activity_id = a4.id)
        days.append(d4)
        d5 = Day(feeling_id = f5.id, activity_id = a5.id)
        days.append(d5)





        db.session.add_all(days)
        db.session.commit()

