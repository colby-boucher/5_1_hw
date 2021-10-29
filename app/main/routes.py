from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.models import Weapons, Types, db

from app.forms import newWeaponForm, newTypeForm

main = Blueprint('main', __name__, template_folder='main_templates')

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/weaponpage', methods =['GET', 'POST'])
def weaponform():
    form = newWeaponForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        longname = form.longname.data
        heat = form.heat.data
        damage = form.damage.data
        size = form.size.data
        cluster_size = form.cluster_size.data
        minimum_range = form.minimum_range.data
        max_short_range = form.max_short_range.data
        max_med_range = form.max_med_range.data
        max_long_range = form.max_long_range.data
        tons = form.tons.data
        crit_slots = form.crit_slots.data
        shots_per_ton = form.shots_per_ton.data
        print(longname)

        new_weapon = Weapons(name = name, longname = longname, heat = heat, damage = damage, size = size, cluster_size = cluster_size, minimum_range = minimum_range, max_short_range = max_short_range, max_med_range = max_med_range, max_long_range = max_long_range, tons = tons, crit_slots = crit_slots, shots_per_ton = shots_per_ton)

        db.session.add(new_weapon)
        db.session.commit()
        flash(f'Succsessfully added {name}')
    elif form.validate_on_submit() == False:
        flash(f"That didn't work")
        print("That didn't work")

    return render_template('weaponpage.html', form = form)

@main.route('/typepage', methods=['GET', 'POST'])
def typeform():
    form = newTypeForm()
    if request.method == 'POST' and form.validate_on_submit():
        abbr_name = form.abbr_name.data
        long_name = form.long_name.data
        print(long_name)
        new_type = Types(abbr_name = abbr_name, long_name = long_name)

        db.session.add(new_type)
        db.session.commit()
        flash(f'Succsessfully added {long_name}')
    elif form.validate_on_submit() == False:
        flash(f"That didn't work")
        print("That didn't work")
    return render_template('typepage.html', form = form)

