from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

from config import db


class Combat(db.Model, SerializerMixin):
    __tablename__ = 'combats'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    enemy_id = db.Column(db.Integer, db.ForeignKey('enemy.id'))
    rnd = db.Column(db.Integer)
    turn = db.Column(db.Integer) #must be 1 or 2
    player_next = db.Column(db.Boolean)
    enemy_action = db.Column(db.String)
    victor = db.Column(db.String)
    # add relationship
    statuses = db.relationship('Status', back_populates = 'combat')
    player = db.relationship('Player', back_populates = 'combat')
    enemy = db.relationship('Enemy', back_populates = 'combat')
    # Add serialization rules
    serialize_rules = ('-statuses.combat', '-player.combat', '-enemy.combat', '-player.statuses', '-enemy.statuses', '-player.known_techs', '-enemy.known_techs' )

    def __repr__(self):
        return f'<Hero {self.id}>'

class Status(db.Model, SerializerMixin):
    __tablename__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True)
    remaining_duration = db.Column(db.Integer)
    affected_stat = db.Column(db.String)
    amnt = db.Column(db.Integer)

    #foreign keys
    combat_id = db.Column(db.Integer, db.ForeignKey('combats.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    # relationships
    combat = db.relationship('Combat', back_populates = 'statuses')
    character = db.relationship('Character', back_populates = 'statuses')
    # serialization rules
    serialize_rules = ('-combat.statuses', '-character.statuses', '-combat.player', '-combat.enemy', '-character.combat', '-character.known_techs' )

    # add validation
    # @validates('affected_stat')
    # def validate_affected_stat(self, key, value):
    #     stats = [] #List of possible stats
    #     if value not in stats:
    #         raise ValueError("error message")
    #     return value

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=True)
    type = db.Column(db.String)
    portrait = db.Column(db.String)

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

    __mapper_args__ = {
        'polymorphic_identity': 'character',
        'polymorphic_on': 'type'
    }

class Player(Character):
    __tablename__ = 'player'
    id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    adv_points = db.Column(db.Integer)


    #relationships
    combat = db.relationship('Combat', uselist=False, back_populates='player')

    # Add serialization rules
    serialize_rules = ('-combat.player', )

    __mapper_args__ = {
        'polymorphic_identity': 'player'
    }

class Enemy(Character):
    __tablename__ = 'enemy'
    id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    actions = db.Column(db.String)
    #crnt_action = db.Column(db.Integer)


    #relationships
    combat = db.relationship('Combat', uselist=False, back_populates='enemy')

    # Add serialization rules
    serialize_rules = ('-combat.enemy', )

    __mapper_args__ = {
        'polymorphic_identity': 'enemy'
    }

class KnownTech(db.Model, SerializerMixin):
    __tablename__ = 'known_techs'

    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    rnk = db.Column(db.Integer)

    #foreign keys
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'))

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
    stat = db.Column(db.String)
    modifier = db.Column(db.Integer)
    amnt = db.Column(db.Integer)

    # relationships
    known_techs = db.relationship('KnownTech', back_populates = 'tech')
    # Add serialization rules
    serialize_rules = ('-known_techs.tech', )

    @validates('target')
    def validate_description(self, key, value):
        if value != 'self' and value != 'opponent':
            raise ValueError("Technique must target 'self' or 'opponent'")
        return value

    @validates('stat')
    def validate_description(self, key, value):
        possible_stats = ["hp", "pwr", "def", "order"]
        if value not in possible_stats:
            raise ValueError("Technique must affect a stat")
        return value