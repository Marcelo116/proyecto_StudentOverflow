from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(512), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    automatica = db.Column(db.Boolean, default=False)
