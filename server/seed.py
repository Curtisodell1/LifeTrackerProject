#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, Activity, Feeling, User, Day

if __name__ == '__main__':
    # fake = Faker()
    with app.app_context():
        # Seed code goes here!
        Activity.query.delete()
        Feeling.query.delete()
        Day.query.delete()
        User.query.delete()

        print("Starting seed...")

    activities = [
        Activity( activity = "Taking a walk", activity_status = "Yes"),
        Activity( activity = "Taking a shower", activity_status = "Yes"),
        Activity( activity = "Going to the gym/ Working out", activity_status = "No"),
        Activity( activity = "Cleaning your home", activity_status = "No"),
        Activity( activity = "Reading a book", activity_status = "Yes")
    ]
    db.session.add_all(activities)

    feelings = [
        Feeling( morning_feeling = 3, afternoon = 6, evening_feeling = 3, description = 'The day started off awful and ended that way. '),
        Feeling( morning_feeling = 6, afternoon = 6, evening_feeling = 9, description = 'An ok start to the day with a great end. '),
        Feeling( morning_feeling = 1, afternoon = 6, evening_feeling = 8, description = 'I thought it would be an awful day but turned out to be great.'),
        Feeling( morning_feeling = 10, afternoon = 6, evening_feeling = 3, description = 'Started off so well but just kept dropping. '),
        Feeling( morning_feeling = 7, afternoon = 6, evening_feeling = 8, description = 'Just a good day.')
    ]