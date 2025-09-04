from main import app
from database import db
from models.user import User
from models.refeicao import Refeicao


with app.app_context():
    db.create_all()  
    print('BD CRIADO')   
    
   