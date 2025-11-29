from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from .database import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

routes = Blueprint("routes", __name__)
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = "routes.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@routes.route("/")
def index():
    return redirect(url_for("routes.login"))

@routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(username=username, password=hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("routes.login"))

    return render_template("register.html")

@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("routes.dashboard"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

@routes.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=current_user.username)

@routes.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("routes.login"))

