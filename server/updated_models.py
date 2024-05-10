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
    base_luck = db.Column(db.Integer)
    spd = db.Column(db.Integer)

    #combat stat block
    crnt_hp = db.Column(db.Integer)
    temp_pwr = db.Column(db.Integer)
    temp_def = db.Column(db.Integer)
    temp_mv = db.Column(db.Integer)
    temp_luck = db.Column(db.Integer)
    position = db.Column(db.Integer)
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
    range = db.Column(db.String) #1234, self, ally, ally/self etc.
    num_targets = db.Column(db.String)
    target_type = db.Column(db.String) #adj, choice, repeat

    effects_json = db.Column(db.String)


    def __init__(self, effects):
        self.effects_json = json.dumps(effects)

    @property
    def effects(self):
        return json.loads(self.effects_json)

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
    technique = db.relationship('Technique', back_populates = 'known_techs')
    # serialization rules
    serialize_rules = ('-character.known_techs', '-technique.known_techs' )


class Status(db.Model, SerializerMixin):
    __tablename__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True)
    remaining_duration = db.Column(db.Integer)
    type = db.Column(db.String)
    #types of Statuses inherit from Status- stat_change, dot, paired (goaded, guarded, mind_meld), others
    stance = db.Column(db.Boolean)

    #foreign keys
    combat_id = db.Column(db.Integer, db.ForeignKey('combats.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    # relationships
    combat = db.relationship('Combat', back_populates = 'statuses')
    character = db.relationship('Character', back_populates = 'statuses')
    # serialization rules
    # serialize_rules = ('-combat.statuses', '-character.statuses', '-combat.player', '-combat.enemy', '-character.combat', '-character.known_techs' )

    __mapper_args__ = {
        'polymorphic_identity': 'status',
        'polymorphic_on': 'type'
    }


class StatChange (Status):
    __tablename__ = 'stat_change'
    
    id = db.Column(db.Integer, db.ForeignKey('statuses.id'), primary_key=True)
    
    affected_stat = db.Column(db.String)
    amnt = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'stat_change'
    }

class DmgOverTime (Status):
    __tablename__ = 'dmg_over_time'
    
    id = db.Column(db.Integer, db.ForeignKey('statuses.id'), primary_key=True)
    name = db.Column(db.String)
    amnt = db.Column(db.Integer)


    __mapper_args__ = {
        'polymorphic_identity': 'dmg_over_time'
    }

class Paired (Status):
    __tablename__ = 'paired'
    
    id = db.Column(db.Integer, db.ForeignKey('statuses.id'), primary_key=True)
    name = db.Column(db.String)
    target_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'paired'
    }

class Other (Status):
    __tablename__ = 'other'
    
    id = db.Column(db.Integer, db.ForeignKey('statuses.id'), primary_key=True)
    name = db.Column(db.String)
    
    stun = db.Column(db.Boolean)

    __mapper_args__ = {
        'polymorphic_identity': 'other'
    }