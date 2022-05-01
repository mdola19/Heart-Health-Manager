from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Profile
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", user=current_user)

@views.route('/stroke', methods=['GET', 'POST'])
#@login_required
def stroke():
    return render_template("stroke.html", user=current_user)

@views.route('/patient', methods=['GET', 'POST'])
#@login_required
def patient():
    if request.method == "POST":
        print(request.form)
        sex = request.form.get('sex')
        age = request.form.get('age')
        work = request.form.get('work')
        married = request.form.get('married')
        residence = request.form.get('urban')
        bmi = request.form.get('bmi')
        hypertension = request.form.get('hyper')
        glucose = request.form.get('glucose')
        smoke = request.form.get('smoke')
        disease = request.form.get('disease')

        #model integration

        percentage = 0

        new_profile = Profile(gender = sex, age = age, hypertension = hypertension, heart_disease = disease, married = married, work_type = work, 
                              residence_type = residence, avg_glucose_level = glucose, bmi = bmi, smoking_status = smoke, percentage=0, user_id = current_user.id)

        db.session.add(new_profile)
        db.session.commit()
        flash('Patient Information Added!', category='sucess')

    return render_template("patient.html", user=current_user)


@views.route('/logs', methods=['GET', 'POST'])
#@login_required
def logs():

    

    return render_template("logs.html", user=current_user)

@views.route('/statistics', methods=['GET', 'POST'])
#@login_required
def statistics():
    return render_template("statistics.html", user=current_user)


