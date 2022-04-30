from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

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
    return render_template("patient.html", user=current_user)

@views.route('/logs', methods=['GET', 'POST'])
#@login_required
def logs():
    return render_template("logs.html", user=current_user)

@views.route('/statistics', methods=['GET', 'POST'])
#@login_required
def statistics():
    return render_template("statistics.html", user=current_user)


