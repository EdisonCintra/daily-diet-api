from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    # Relacionamento 1:N com refeições
    refeicoes = db.relationship("Refeicao", backref="usuario", lazy=True)
