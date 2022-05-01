from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Profile
from . import db
import pickle
import numpy as np

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html", user=current_user)

    
strokemodel = pickle.load(open('Heart_Health_Website/Machine Learning Model\StrokeModel.pickle', 'rb'))
@views.route('/patient', methods=['GET', 'POST'])
#@login_required
def patient():
    gender = {"Male": 1, "Female" : 0}
    residence = {"Urban" : 1, "Rural": 0}
    smoking_status = {"Unknown" : 0, "Formerly Smoked":1, "Never Smoked":2, "Smokes" : 3}
    work_type = {"Government Job" : 0, "Never Worked" : 1, "Private" : 2, "Self-Employed" : 3, "Children": 4}
    yes_no = {"No": 0, "Yes": 1}
    user_first_name = str(current_user.firstName)
    if request.method == "POST":
        print(request.form)
        sex = request.form.get('sex')
        age = request.form.get('age')
        work = request.form.get('work')
        married = request.form.get('married') 
        urban = request.form.get('urban')
        bmi = request.form.get('bmi')
        hypertension = request.form.get('hyper')
        glucose = request.form.get('glucose')
        smoke = request.form.get('smoke')
        disease = request.form.get('disease')



        arr = np.array([sex, age, hypertension, disease, married, work, urban, glucose, bmi, smoke])
        arr[0] = gender[arr[0]]
        arr[2] = yes_no[arr[2]]
        arr[3] = yes_no[arr[3]]
        arr[4] = yes_no[arr[4]]
        arr[5] = work_type[arr[5]]
        arr[6] = residence[arr[6]]
        arr[9] = smoking_status[arr[9]]
        arr = np.expand_dims(arr, axis=0)
        pred = strokemodel.predict(arr)
        probs = strokemodel.predict_proba(arr)
        idx = np.argmax(probs)
        confidence = probs.flatten()[idx]
        confidence = round(confidence, 2)
        confidence *= 100
        new_profile = Profile(gender = sex, age = age, hypertension = hypertension, heart_disease = disease, married = married, work_type = work, 
                               residence_type = 'Urban', avg_glucose_level = glucose, bmi = bmi, smoking_status = smoke, percentage = confidence, user_id = current_user.id)

        db.session.add(new_profile)
        db.session.commit()
        flash('Patient Information Added!', category='sucess')

        print(current_user.profiles)

    
        return render_template("patient.html", user=current_user, data=pred, confidence = confidence, firstName = user_first_name)
    return render_template("patient.html", user=current_user, firstName = user_first_name)

@views.route('/logs', methods=['GET', 'POST'])
#@login_required


def logs():
    user_first_name = str(current_user.firstName)
    

    return render_template("logs.html", user=current_user, firstName = user_first_name)

@views.route('/statistics', methods=['GET', 'POST'])
#@login_required
def statistics():
    user_first_name = str(current_user.firstName)
    

    return render_template("statistics.html", user=current_user, firstName = user_first_name)

@views.route('/stroke', methods=['GET', 'POST'])
def stroke():
    user_first_name = str(current_user.firstName)


    return render_template("stroke.html", firstName = user_first_name)
