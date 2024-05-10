# Local imports
from app import app
from models import *

if __name__ == '__main__':
    with app.app_context():
        print("deleting data")
        Combat.query.delete()
        Character.query.delete()
        Technique.query.delete()
        KnownTech.query.delete()
        Status.query.delete()
        StatChange.query.delete()
        DmgOverTime.query.delete()
        Paired.query.delete()
        Other.query.delete()

        print("Data deleted. Starting seed...")
        # Seed code goes here!
        new_characters = [
            Character(
                id = 1,
                hero_class = "Mage"

            )
        ]

        db.session.add_all(new_characters)
        db.session.commit()
        
        mage_techs = [
            Technique(
                name = "Firebolt",
                hero_class = "Mage",
                position = "432",
                range = "234",
                num_targets = 1,
                target_type = "choice",
                effects = [
                    Effect(description = "Dmg", amnt = -2),
                    Effect(description = "Brn", amnt = -3, status = "dot")
                ]
            ),
            Technique(
                name = "Flame Splash",
                hero_class = "Mage",
                position = "43",
                range = "34",
                num_targets = 2,
                target_type = "adj",
                effects = [
                    Effect(description = "Dmg", amnt = -3),
                    Effect(description = "Brn", amnt = -3, status = "dot")
                ]
            ),
            Technique(
                name = "Conflagration",
                hero_class = "Mage",
                position = "1",
                range = "1",
                num_targets = 2,
                target_type = "adj",
                effects = [
                    Effect(description = "Back", amnt = 2),
                    Effect(description = "Dmg", amnt = 4),
                    Effect(description = "Knockback", amnt = 1, chance = 4)
                ]
            ),
            Technique(
                name = "Cauterize",
                hero_class = "Mage",
                position = "432",
                range = "ally",
                num_targets = 1,
                target_type = "choice",
                effects = [
                    Effect(description = "Heal", amnt = 0, mod = 2),
                    Effect(description = "Brn", amnt = 0, status = "dot")
                ]
            ),
            Technique(
                name = "Icy Lunge",
                hero_class = "Mage",
                position = "43",
                range = "123",
                num_targets = 3,
                target_type = "adj",
                effects = [
                    Effect(description = "Forward", amnt = 1),
                    Effect(description = "Dmg", amnt = -2)
                ]
            ),
            Technique(
                name = "Freeze",
                hero_class = "Mage",
                position = "43",
                range = "234",
                num_targets = 1,
                target_type = "choice",
                effects = [
                    Effect(description = "Dmg", amnt = -4),
                    Effect(description = "Frozen", dur = 1, chance = 4, status = "frozen")
                ]
            ),
            Technique(
                name = "Ice Block",
                hero_class = "Mage",
                position = "4321",
                range = "self",
                num_targets = 1,
                target_type = "choice",
                effects = [
                    Effect(description = "Buff", amnt = 8, dur = 1, stat = "def", status = "stat"),
                    Effect(description = "Frozen", dur = 1, status = "frozen")
                ]
            )

        ]

        db.session.add_all(mage_techs)
        db.session.commit()


        print("seeded")