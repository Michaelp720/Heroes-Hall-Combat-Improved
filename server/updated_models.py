from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db


class Combat(db.Model, SerializerMixin):
    __tablename__ = 'combat'

    id = db.Column(db.Integer, primary_key=True)
    rnd = db.Column(db.Integer)
    turn = db.Column(db.Integer) #1-8

    # add relationships
    statuses = db.relationship('Status', back_populates = 'combat')
    left_chars = db.relationship('Character', back_populates = 'combat')
    right_chars = db.relationship('Character', back_populates = 'combat')
    # Add serialization rules
    # serialize_rules = ('-statuses.combat', '-player.combat', '-enemy.combat', '-player.statuses', '-enemy.statuses', '-player.known_techs', '-enemy.known_techs' )

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True) 
    hero_class = db.Column(db.String)

    #base stat block
    max_hp = db.Column(db.Integer)
    base_pwr = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    base_mv = db.Column(db.Integer)
    spd = db.Column(db.Integer)

    #combat stat block
    crnt_hp = db.Column(db.Integer)
    temp_pwr = db.Column(db.Integer)
    temp_def = db.Column(db.Integer)
    temp_mv = db.Column(db.Integer)
    order = db.Column(db.Integer)

    # add relationships
    statuses = db.relationship('Status', back_populates = 'character')
    known_techs = db.relationship('KnownTech', back_populates = 'character')
    combat = db.relationship('Combat', uselist=False, back_populates='character')

    # Add serialization rules
    # serialize_rules = ('-statuses.character', '-known_techs.character')

class Technique(db.Model, SerializerMixin):
    __tablename__ = 'techniques'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hero_class = db.Column(db.String)

    position = db.Column(db.String) #4321
    range = db.Column(db.String) #1234, self, ally etc.
    num_targets = db.Column(db.String)
    target_type = db.Column(db.String) #adj, choice, repeat

    effects_json = db.Column(db.String)


    def __init__(self, effects):
        self.effects_json = json.dumps(effects)

    @property
    def effects(self):
        return json.loads(self.effects_json)