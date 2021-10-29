from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField, SubmitField, IntegerField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField #https://github.com/wtforms/wtforms-sqlalchemy
from wtforms.validators import DataRequired
from .models import getTypes


class newWeaponForm(FlaskForm): #Not sure if I'd actually have a form for this
    name = StringField('Abbreviated name', validators = [DataRequired()])
    longname = StringField('Full Name', validators = [DataRequired()])
    heat = IntegerField('Heat per turn', validators = [DataRequired()])
    damage = IntegerField('Damage per projectile')
    size = IntegerField('Weapon size (leave blank if not cluster weapon)')
    cluster_size = IntegerField('Number of hits for each cluster')
    minimum_range = IntegerField('Minimum range')
    max_short_range = IntegerField('Maximum short range')
    max_med_range = IntegerField('Maximum medium range')
    max_long_range = IntegerField('Maximum long range')
    tons = IntegerField('Tonnage', validators = [DataRequired()])
    crit_slots = IntegerField('Critical slots', validators = [DataRequired()])
    shots_per_ton = IntegerField('Shots per ton')
    types = QuerySelectMultipleField('Assiociated Types', validators = [DataRequired()], query_factory = getTypes(), get_label = 'abbr_name')
    submit_button = SubmitField()

class newTypeForm(FlaskForm):
    abbr_name = StringField('Abbreviated name', validators = [DataRequired()])
    long_name = StringField ('Full name', validators = [DataRequired()])
    submit_button = SubmitField()