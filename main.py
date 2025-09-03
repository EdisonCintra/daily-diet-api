import os
from models.user import User
from models.refeicao import Refeicao
from flask import Flask, send_file, jsonify, request
from database import db
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login' #?

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso."})

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    nome = data.get("nome")
    senha = data.get("senha")
    if nome and senha:
        user = User.query.filter_by(nome=nome).first()
        if user and user.senha == senha:
            login_user(user)
            return jsonify({"message": "Login realizado com sucesso."})
    return jsonify({"message": "Credenciais inválidas."}), 401



@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    nome = data.get("nome")
    senha = data.get("senha")
    if nome and senha:
        new_user = User(nome=nome, senha=senha)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuário criado com sucesso"}), 201

    return jsonify({"message" : "Erro ao criar o usuário"}), 400

@app.route('/create_refeicao', methods=['POST'])
@login_required
def create_refeicao():
    data = request.json
    nome_refeicao = data.get("nome_refeicao")
    descricao = data.get("descricao")
    dentro_dieta = data.get("dentro_dieta")
    data_hora = datetime.now()
    user = current_user.id

    new_refeicao = Refeicao(
        nome_refeicao=nome_refeicao,
        descricao=descricao,
        data_hora=data_hora,
        dentro_dieta=dentro_dieta,
        user_id=user
    )
    db.session.add(new_refeicao)
    db.session.commit()

    return jsonify({"message": "Refeição criada com sucesso"}), 201


def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)