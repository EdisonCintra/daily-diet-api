class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    # Relacionamento 1:N com refeições
    refeicoes = db.relationship("Refeicao", backref="usuario", lazy=True)
