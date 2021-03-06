from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Activity, Save
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.username, user=current_user)


@views.route("/activities")
@login_required
def activities():
    return render_template("activities.html", user=current_user)


@views.route("/create", methods=['GET', 'POST'])
@login_required
def create_post():

    if request.method == "POST":
        # Update html file
        choice = request.form.get('choice')

        # Store informations
        types = request.form.get('type')
        save = Save(types)

    else:
        choice = ""
        flash("Choice training type", category="succes")

    return render_template('create_post.html', user=current_user, type=choice)
