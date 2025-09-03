from database import db

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_refeicao = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    dentro_dieta = db.Column(db.Boolean, nullable=False)
    
    # FK para User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
