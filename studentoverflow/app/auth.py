from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Usuario
from app import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = Usuario.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("main.index"))
        else:
            flash("Correo o contraseña incorrecta")
    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        if Usuario.query.filter_by(email=email).first():
            flash("El correo ya está registrado")
            return redirect(url_for("auth.register"))
        new_user = Usuario(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.index"))