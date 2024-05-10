

class Effect:
    def __init__(self, description, amnt = 0, dur = 0, chance = 0, mod = 1, stat = None, status = None):
        self.description = description
        self.amnt = amnt
        self.dur = dur
        self.chance = chance
        self.mod = mod
        self.stat = stat
        self.status = status #dot, paired, other, stat change

    #for calculating effects that use pwr ie dmg, heal, dot
    def calculate_amnt(self, pwr):
        return self.mod * pwr + amnt
        


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
        Effect("Brn", -3, 0, False, 1, "dot")
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
)