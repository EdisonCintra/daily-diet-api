# Daily Diet API

Este projeto consiste em uma API para **gerenciamento de refeições** e acompanhamento de dietas, permitindo criar, editar, listar e deletar refeições de usuários cadastrados. A API foi desenvolvida utilizando **Flask** e **Flask-Login** para autenticação de usuários.

## Funcionalidades

- Cadastro de usuários (nome e senha).  
- Login e logout de usuários com gerenciamento de sessão.  
- Criação de refeições com nome, descrição, se está dentro da dieta e timestamp.  
- Edição de refeições existentes.  
- Listagem de todas as refeições de um usuário ou de uma refeição específica.  
- Exclusão de refeições.  

## Tecnologias Utilizadas

- Python 3.11  
- Flask  
- Flask-Login  
- Flask-SQLAlchemy  
- SQLite  

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.11 ou superior  
- pip  

## Instalação e Execução

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/daily-diet-api


Acesse a pasta do projeto:

cd daily-diet-api


Crie e ative um ambiente virtual:

python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


Crie o banco de dados utilizando o script shell_create_db.py:

python shell_create_db.py


Saída esperada:

BD CRIADO


Execute a API:

python main.py


A API estará disponível em http://127.0.0.1:5000.

💻 Shell e Testes
1️⃣ shell_create_db.py

Cria o banco de dados database.db e todas as tabelas (User e Refeicao).

Deve ser executado antes de rodar a API para garantir que todas as tabelas existam.

2️⃣ teste.py

Automatiza requisições HTTP para testar todas as rotas da API.

Permite validar rapidamente o fluxo completo:

Criar usuário

Login do usuário

Criar várias refeições

Listar todas as refeições do usuário

Listar uma refeição específica

Editar uma refeição

Deletar uma refeição

Logout

Ideal para verificar se todas as funcionalidades estão funcionando sem precisar de ferramentas externas como Postman.

Como usar:

python teste.py


Exemplo de saída:

=== Criar Usuário ===
201 {"message": "Usuário criado com sucesso"}

=== Login ===
200 {"message": "Login realizado com sucesso."}

=== Criar Refeição ===
201 {"message": "Refeição criada com sucesso"}

=== Listar Refeições do Usuário ===
200 [{"id":1,"nome_refeicao":"Almoço",...}, ...]

=== Editar Refeição ===
201 {"message": "Refeição editada com sucesso"}

=== Deletar Refeição ===
200 {"message": "Refeição deletada com sucesso"}

=== Logout ===
200 {"message": "Logout realizado com sucesso."}

Uso da API

Crie um usuário com /create_user.

Faça login com /login.

Crie refeições com /create_refeicao.

Liste as refeições do usuário com /refeicao_por_user.

Liste uma refeição específica com /listar_refeicao/<id>.

Edite refeições com /editar-refeicao/<id>.

Delete refeições com /delete_refeicao/<id>.

Faça logout com /logout.

Todas as rotas de criação, edição, listagem e exclusão de refeições requerem autenticação.

Licença

Este projeto está licenciado sob a Licença MIT
.