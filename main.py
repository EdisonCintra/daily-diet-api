import os
from models.user import User
from models.refeicao import Refeicao
from flask import Flask, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)