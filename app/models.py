from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship


db = SQLAlchemy()


# Flask-SQLAlchemy suggests using db.Table here(https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) for helper tables,
# But I can't get flask-migrate to pick up on anything made with that class
class Weapontypes(db.Model):
    weaponname = db.Column('weapon_name', db.String(10), db.ForeignKey('weapons.name'), primary_key = True)
    weapontype = db.Column('type', db.String(2), db.ForeignKey('types.abbr_name'), primary_key = True)

class Weapons(db.Model):
# Thinking about this in terms of potential final project (tabletop Battletech record sheet manager thing)
    name = db.Column(db.String(10), primary_key = True)
    longname = db.Column(db.String(50), nullable = False, unique = True)
    heat = db.Column(db.Integer, nullable = False)
    damage = db.Column(db.Integer, nullable = True)
    size = db.Column(db.Integer, nullable = True)
    cluster_size = db.Column(db.Integer, nullable = True)
    minimum_range = db.Column(db.Integer, nullable = True)
    max_short_range = db.Column(db.Integer, nullable = True)
    max_med_range = db.Column(db.Integer, nullable = True)
    max_long_range = db.Column(db.Integer, nullable = True)
    tons = db.Column(db.Integer, nullable = False)
    crit_slots = db.Column(db.Integer, nullable = False)
    shots_per_ton = db.Column(db.Integer, nullable = True)
    types = db.relationship("Types", secondary=Weapontypes)

    def __repr__(self) -> str:  #What an odd way for this to autocomplete, calling itself?
        return '<Weapon %r>' %self.name


class Types(db.Model):
    abbr_name = db.Column(db.String(2), primary_key = True)
    long_name = db.Column(db.String(50), nullable = False, unique = True)

    def __repr__(self):
        return '<Type %r>' %self.abbr_name

def getTypes():
    return Types.query