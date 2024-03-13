#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("deleting data")
        Character.query.delete()
        Player.query.delete()

        print("Data deleted. Starting seed...")
        # Seed code goes here!
        new_players = [
            Player(
                name = "Aragorn"
            )
        ]

        db.session.add_all(new_players)
        db.session.commit()

        print("seeded")