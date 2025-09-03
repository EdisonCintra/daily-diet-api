import os
from models.user import User
from models.refeicao import Refeicao
from flask import Flask, send_file, jsonify, request
from database import db
from flask_login import LoginManager, login_user, current_user, login_required


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

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)