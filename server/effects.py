

class Effect:
    def __init__(self, description, amnt_dur, chance = False, mod = 1, status = False):
        self.description = description
        self.amnt_dur = amnt_dur
        self.chance = chance
        self.mod = mod
        self.status = status #dot, paired, other, stat change

    #for calculating effects that use pwr
    def calculate_amnt(self, pwr):
        return self.mod * pwr + amnt_dur
        


#example- firebolt

Technique(
    name = "Firebolt",
    hero_class = "Mage",
    position = "432",
    range = "234",
    num_targets = 1,
    target_type = "choice",
    effects = [
        Effect("Dmg", -2),
        Effect("Brn", -3, False, 1, "dot")
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
        Effect("Dmg", -3),
        Effect("Brn", -3, False, 1, "dot")
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
        Effect("Back", 2),
        Effect("Dmg", 4),
        Effect("Knockback", 1, 4)
    ]
),