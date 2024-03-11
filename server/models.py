from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db


class Combat(db.Model, SerializerMixin):
    __tablename__ = 'combats'

    id = db.Column(db.Integer, primary_key=True)
    rnd = db.Column(db.Integer) 

    # add relationship
    statuses = db.relationship('Status', back_populates = 'combat')
    # Add serialization rules
    serialize_rules = ('-statuses.combat', )

    def __repr__(self):
        return f'<Hero {self.id}>'

class Status(db.Model, SerializerMixin):
    __tablename__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True)
    remaining_duration = db.Column(db.Integer)
    affected_stat = db.Column(db.String)

    #foreign keys
    combat_id = db.Column(db.Integer, db.ForeignKey('combats.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    # relationships
    combat = db.relationship('combat', back_populates = 'statuses')
    character = db.relationship('character', back_populates = 'statuses')
    # serialization rules
    serialize_rules = ('-combat.statuses', '-character.statuses' )

    # add validation
    # @validates('affected_stat')
    # def validate_affected_stat(self, key, value):
    #     stats = [] #List of possible stats
    #     if value not in list:
    #         raise ValueError("error message")
    #     return value

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String)
    #portrait = db.Column(db.String)

    #base stat block
    max_hp = db.Column(db.Integer)
    base_pwr = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    spd = db.Column(db.Integer)

    #combat stat block
    crnt_hp = db.Column(db.Integer)
    temp_pwr = db.Column(db.Integer)
    temp_def = db.Column(db.Integer)
    order = db.Column(db.Integer)

    # add relationships
    statuses = db.relationship('Status', back_populates = 'character')
    known_techs = db.relationship('KnownTech', back_populates = 'character')
    # Add serialization rules
    serialize_rules = ('-statuses.character', '-known_techs.character')

class KnownTech(db.Model, SerializerMixin):
    __tablename__ = 'known_techs'

    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    rnk = db.Column(db.Integer)

    #foreign keys
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    tech_id = db.Column(db.Integer, db.ForeignKey('techniques.id'))

    # relationships
    character = db.relationship('Character', back_populates = 'known_techs')
    tech = db.relationship('Technique', back_populates = 'known_techs')
    # serialization rules
    serialize_rules = ('-character.known_techs', '-tech.known_techs' )

class Technique(db.Model, SerializerMixin):
    __tablename__ = 'techs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    target = db.Column(db.String)
    duration = db.Column(db.Integer)
    status = db.Column(db.String)
    amnt = db.Column(db.Integer)

    # relationships
    known_techs = db.relationship('KnownTech', back_populates = 'tech')
    # Add serialization rules
    serialize_rules = ('-known_techs.tech', )