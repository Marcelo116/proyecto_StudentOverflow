from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import Pregunta, Respuesta, Usuario
from app import db
import requests
bp = Blueprint("main", __name__)

@bp.route("/")
def index():
   preguntas = Pregunta.query.all()
   return render_template("index.html", preguntas=preguntas)

@bp.route("/preguntar", methods=["GET", "POST"])
def preguntar():
    if "user_id" not in session:
        flash("Inicia sesión para publicar una pregunta.")
        return redirect(url_for("auth.login"))
    if request.method == "POST":
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        nueva = Pregunta(titulo=titulo, descripcion=descripcion, usuario_id=session["user_id"])
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("preguntar.html")


@bp.route("/pregunta/<int:id>", methods=["GET", "POST"])
def detalle_pregunta(id):
    pregunta = Pregunta.query.get_or_404(id)
    respuestas = Respuesta.query.filter_by(pregunta_id=id).all()

    if request.method == "POST":
        if "user_id" not in session:
            flash("Inicia sesión para responder.")
            return redirect(url_for("auth.login"))
        contenido = request.form["contenido"]
        r = Respuesta(contenido=contenido, pregunta_id=id, autor_id=session["user_id"])
        db.session.add(r)
        db.session.commit()
        return redirect(url_for("main.detalle_pregunta", id=id))

    if not respuestas:
        resumen = consultar_wikipedia(pregunta.titulo)
        if resumen:
            auto = Respuesta(contenido=resumen, pregunta_id=id, automatica=True)
            db.session.add(auto)
            db.session.commit()
            respuestas = [auto]
    return render_template("detalle_pregunta.html", pregunta=pregunta, respuestas=respuestas)

def consultar_wikipedia(query):
    try:
        response = requests.get(f"https://es.wikipedia.org/api/rest_v1/page/summary/{query}")
        if response.status_code == 200:
            data = response.json()
            return data.get("extract")
    except:
        return None