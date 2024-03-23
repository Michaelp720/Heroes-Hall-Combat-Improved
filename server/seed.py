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
        Enemy.query.delete()
        Technique.query.delete()
        KnownTech.query.delete()
        Combat.query.delete()
        Status.query.delete()

        print("Data deleted. Starting seed...")
        # Seed code goes here!
        new_players = [
            Player(
                id = 1,
                name = "Aragorn",
                portrait = 'Aragorn.jpg',
                max_hp = 18,
                base_pwr = 4,
                base_def = 1,
                spd = 7,
                crnt_hp = 18,
                temp_pwr = 4,
                temp_def = 1,
                order = None
            ),
            Player(
                id = 5,
                name = "Kvothe",
                portrait = 'Kvothe.jpg',
                max_hp = 13,
                base_pwr = 4,
                base_def = 0,
                spd = 9,
                crnt_hp = 13,
                temp_pwr = 4,
                temp_def = 0,
                order = None
            )
        ]

        db.session.add_all(new_players)
        db.session.commit()

        new_enemies = [
            Enemy(
                id = 2,
                actions = "211",
                name = "Balewolf",
                portrait = 'Balewolf.jpeg',
                max_hp = 10,
                base_pwr = 4,
                base_def = 0,
                spd = 15,
                crnt_hp = 10,
                temp_pwr = 4,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 3,
                actions = "1",
                name = "Lostling",
                max_hp = 6,
                base_pwr = 3,
                base_def = 1,
                spd = 2,
                crnt_hp = 6,
                temp_pwr = 3,
                temp_def = 1,
                order = None
            ),
            Enemy(
                id = 4,
                actions = "212",
                name = "Wardeer",
                max_hp = 6,
                base_pwr = 4,
                base_def = 1,
                spd = 8,
                crnt_hp = 6,
                temp_pwr = 4,
                temp_def = 1,
                order = None
            ),
            Enemy(
                id = 6,
                actions = "221",
                name = "Greenbreather",
                max_hp = 5,
                base_pwr = 3,
                base_def = 1,
                spd = 2,
                crnt_hp = 5,
                temp_pwr = 3,
                temp_def = 1,
                order = None
            ),
            Enemy(
                id = 7,
                actions = "1",
                name = "Sunsparrow",
                max_hp = 2,
                base_pwr = 2,
                base_def = 0,
                spd = 9,
                crnt_hp = 2,
                temp_pwr = 2,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 8,
                actions = "1222222222",
                name = "Shadowcat",
                max_hp = 7,
                base_pwr = 4,
                base_def = 0,
                spd = 12,
                crnt_hp = 7,
                temp_pwr = 4,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 9,
                actions = "12111",
                name = "Razorboar",
                max_hp = 6,
                base_pwr = 3,
                base_def = 2,
                spd = 6,
                crnt_hp = 6,
                temp_pwr = 3,
                temp_def = 2,
                order = None
            ),
            Enemy(
                id = 10,
                actions = "121",
                name = "Shoddy Construct",
                max_hp = 12,
                base_pwr = 3,
                base_def = 0,
                spd = 15,
                crnt_hp = 6,
                temp_pwr = 3,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 11,
                actions = "2111",
                name = "Bloodrake",
                max_hp = 10,
                base_pwr = 3,
                base_def = 2,
                spd = 6,
                crnt_hp = 10,
                temp_pwr = 3,
                temp_def = 2,
                order = None
            ),
            Enemy(
                id = 12,
                actions = "1",
                name = "Raveneye",
                max_hp = 2,
                base_pwr = 3,
                base_def = 0,
                spd = 2,
                crnt_hp = 2,
                temp_pwr = 3,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 13,
                actions = "21222",
                name = "Misting",
                max_hp = 6,
                base_pwr = 3,
                base_def = 0,
                spd = 3,
                crnt_hp = 6,
                temp_pwr = 3,
                temp_def = 0,
                order = None
            ),
            Enemy(
                id = 14,
                actions = "211111",
                name = "Great Elk",
                max_hp = 7,
                base_pwr = 3,
                base_def = 3,
                spd = 7,
                crnt_hp = 7,
                temp_pwr = 3,
                temp_def = 3,
                order = None
            ),
            Enemy(
                id = 15,
                actions = "1323",
                name = "Moonbear",
                max_hp = 9,
                base_pwr = 4,
                base_def = 1,
                spd = 6,
                crnt_hp = 9,
                temp_pwr = 4,
                temp_def = 1,
                order = None
            ),
            Enemy(
                id = 16,
                actions = "12222",
                name = "Cloakhart",
                max_hp = 6,
                base_pwr = 4,
                base_def = 0,
                spd = 10,
                crnt_hp = 6,
                temp_pwr = 4,
                temp_def = 0,
                order = None
            )
        ]

        db.session.add_all(new_enemies)
        db.session.commit()

        new_techs = [
            Technique(
                id = 1,
                name = "Slash",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0 #pwr
            ),
            Technique(
                id = 2,
                name = "Snarl",
                target = "opponent",
                duration = 3,
                stat = "def",
                modifier = 0, 
                amnt = -3
            ),
            Technique(
                id = 3,
                name = "Parry",
                target = "self",
                duration = 2,
                stat = "def",
                modifier = 0,
                amnt = 2 #0pwr +2
            ),
            Technique(
                id = 4,
                name = "Recover",
                target = "self",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = -1 #pwr -1
            ),
            Technique(
                id = 5,
                name = "Sprint",
                target = "self",
                duration = 0,
                stat = "order",
                modifier = 0,
                amnt = 1
            ),
            Technique(
                id = 6,
                name = "Draining Touch",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            ),
            Technique(
                id = 7,
                name = "Amplify",
                target = "self",
                duration = 2,
                stat = "pwr",
                modifier = 0,
                amnt = 3
            ),
            Technique(
                id = 8,
                name = "Discord",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = -1
            ),
            Technique(
                id = 9,
                name = "Lullaby",
                target = "opponent",
                duration = 2,
                stat = "pwr",
                modifier = 0,
                amnt = -2
            ),
            Technique(
                id = 10,
                name = "Horn Glow",
                target = "self",
                duration = 1,
                stat = "def",
                modifier = 0,
                amnt = 10
            ),
            Technique(
                id = 11,
                name = "Kick",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = -1
            ),
            Technique(
                id = 12,
                name = "Greenbreath",
                target = "self",
                duration = 0,
                stat = "hp",
                modifier = 0,
                amnt = 4
            ),
            Technique(
                id = 13,
                name = "Poison Cloud",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            ),
            Technique(
                id = 14,
                name = "Dart",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            ),
            Technique(
                id = 15,
                name = "Pounce",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 2,
                amnt = 0
            ),
            Technique(
                id = 16,
                name = "Claw",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = -1
            ),
            Technique(
                id = 17,
                name = "Gore",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            ),
            Technique(
                id = 18,
                name = "Charge",
                target = "self",
                duration = 0,
                stat = "order",
                modifier = 0,
                amnt = 1
            ),
            Technique(
                id = 19,
                name = "Leak",
                target = "self",
                duration = 0,
                stat = "hp",
                modifier = 0,
                amnt = -1
            ),
            Technique(
                id = 20,
                name = "Sputter",
                target = "self",
                duration = 1,
                stat = "def",
                modifier = 0,
                amnt = -2
            ),
            Technique(
                id = 21,
                name = "Bloodrush",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = +2
            ),
            Technique(
                id = 22,
                name = "Bloodmist",
                target = "opponent",
                duration = 3,
                stat = "def",
                modifier = 0,
                amnt = -3
            ),
            Technique(
                id = 23,
                name = "Muffle",
                target = "opponent",
                duration = 4,
                stat = "pwr",
                modifier = 0,
                amnt = -1
            ),
            Technique(
                id = 24,
                name = "Envelop",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = +1
            ),
            Technique(
                id = 25,
                name = "Moonbeam",
                target = "opponent",
                duration = 1,
                stat = "def",
                modifier = 0,
                amnt = -5
            ),
            Technique(
                id = 26,
                name = "Bask",
                target = "self",
                duration = 0,
                stat = "hp",
                modifier = 0,
                amnt = 4
            ),
            Technique(
                id = 27,
                name = "Moonclaw",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            ),
            Technique(
                id = 28,
                name = "Fade",
                target = "self",
                duration = 4,
                stat = "def",
                modifier = 0,
                amnt = 1
            ),
            Technique(
                id = 29,
                name = "Snipe",
                target = "opponent",
                duration = 0,
                stat = "hp",
                modifier = 1,
                amnt = 0
            )
        ]

        db.session.add_all(new_techs)
        db.session.commit()

        new_known_techs = [
            KnownTech(
                id = 1,
                slot = 1,
                rnk = 0,
                character_id = 1,
                tech_id = 1
            ),
            KnownTech(
                id = 2,
                slot = 2,
                rnk = 0,
                character_id = 1,
                tech_id = 3
            ),
            KnownTech(
                id = 3,
                slot = 3,
                rnk = 0,
                character_id = 1,
                tech_id = 4
            ),
            KnownTech(
                id = 4,
                slot = 1,
                rnk = 0,
                character_id = 2,
                tech_id = 1
            ),
            KnownTech(
                id = 5,
                slot = 2,
                rnk = 0,
                character_id = 2,
                tech_id = 2
            ),
            KnownTech(
                id = 6,
                slot = 4,
                rnk = 0,
                character_id = 1,
                tech_id = 5
            ),
            KnownTech(
                id = 7,
                slot = 1,
                rnk = 0,
                character_id = 3,
                tech_id = 6
            ),
            KnownTech(
                id = 8,
                slot = 1,
                rnk = 0,
                character_id = 5,
                tech_id = 7
            ),
            KnownTech(
                id = 9,
                slot = 2,
                rnk = 0,
                character_id = 5,
                tech_id = 8
            ),
            KnownTech(
                id = 10,
                slot = 3,
                rnk = 0,
                character_id = 5,
                tech_id = 9
            ),
            KnownTech(
                id = 11,
                slot = 1,
                rnk = 0,
                character_id = 4,
                tech_id = 10
            ),
            KnownTech(
                id = 12,
                slot = 2,
                rnk = 0,
                character_id = 4,
                tech_id = 11
            ),
            KnownTech(
                id = 13,
                slot = 1,
                rnk = 0,
                character_id = 6,
                tech_id = 12
            ),
            KnownTech(
                id = 14,
                slot = 2,
                rnk = 0,
                character_id = 6,
                tech_id = 12
            ),
            KnownTech(
                id = 15,
                slot = 1,
                rnk = 0,
                character_id = 7,
                tech_id = 14
            ),
            KnownTech(
                id = 16,
                slot = 1,
                rnk = 0,
                character_id = 8,
                tech_id = 15
            ),
            KnownTech(
                id = 17,
                slot = 2,
                rnk = 0,
                character_id = 8,
                tech_id = 16
            ),
            KnownTech(
                id = 18,
                slot = 1,
                rnk = 0,
                character_id = 9,
                tech_id = 17
            ),
            KnownTech(
                id = 19,
                slot = 2,
                rnk = 0,
                character_id = 9,
                tech_id = 18
            ),
            KnownTech(
                id = 20,
                slot = 1,
                rnk = 0,
                character_id = 10,
                tech_id = 19
            ),
            KnownTech(
                id = 21,
                slot = 2,
                rnk = 0,
                character_id = 10,
                tech_id = 20
            ),
            KnownTech(
                id = 22,
                slot = 1,
                rnk = 0,
                character_id = 11,
                tech_id = 21
            ),
            KnownTech(
                id = 23,
                slot = 2,
                rnk = 0,
                character_id = 11,
                tech_id = 22
            ),
            KnownTech(
                id = 24,
                slot = 1,
                rnk = 0,
                character_id = 12,
                tech_id = 14
            ),
            KnownTech(
                id = 25,
                slot = 1,
                rnk = 0,
                character_id = 13,
                tech_id = 23
            ),
            KnownTech(
                id = 26,
                slot = 2,
                rnk = 0,
                character_id = 13,
                tech_id = 24
            ),
            KnownTech(
                id = 27,
                slot = 1,
                rnk = 0,
                character_id = 14,
                tech_id = 17
            ),
            KnownTech(
                id = 28,
                slot = 2,
                rnk = 0,
                character_id = 14,
                tech_id = 18
            ),
            KnownTech(
                id = 29,
                slot = 1,
                rnk = 0,
                character_id = 15,
                tech_id = 25
            ),
            KnownTech(
                id = 30,
                slot = 2,
                rnk = 0,
                character_id = 15,
                tech_id = 26
            ),
            KnownTech(
                id = 31,
                slot = 3,
                rnk = 0,
                character_id = 15,
                tech_id = 27
            ),
            KnownTech(
                id = 32,
                slot = 1,
                rnk = 0,
                character_id = 16,
                tech_id = 28
            ),
            KnownTech(
                id = 33,
                slot = 2,
                rnk = 0,
                character_id = 16,
                tech_id = 29
            )
        ]

        db.session.add_all(new_known_techs)
        db.session.commit()

        # new_combats = [
        #     Combat(
        #         id = 1,
        #         player_id = 1,
        #         enemy_id = 2,
        #         rnd = 1
        #     )
        # ]

        # db.session.add_all(new_combats)
        # db.session.commit()

        # new_status = Status(
        #     remaining_duration = 2,
        #     affected_stat = "def",
        #     amnt = -2,
        #     combat_id = 1,
        #     character_id = 1
        # )

        # db.session.add(new_status)
        # db.session.commit()
        

        print("seeded")