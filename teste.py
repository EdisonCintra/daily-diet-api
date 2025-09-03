import requests

BASE_URL = "http://127.0.0.1:5000"

# Cria sessão para manter cookies da sessão
s = requests.Session()

# -------------------------------
# 1️⃣ Criar usuário
# -------------------------------
print("\n=== Criar Usuário ===")
r = s.post(f"{BASE_URL}/create_user", json={
    "nome": "edison",
    "senha": "1234"
})
print(r.status_code, r.text)

# -------------------------------
# 2️⃣ Login
# -------------------------------
print("\n=== Login ===")
r = s.post(f"{BASE_URL}/login", json={"nome": "edison", "senha": "1234"})
print(r.status_code, r.text)

# -------------------------------
# 3️⃣ Criar refeição
# -------------------------------
print("\n=== Criar Refeição ===")
r = s.post(f"{BASE_URL}/create_refeicao", json={
    "nome_refeicao": "Almoço",
    "descricao": "Arroz, feijão e frango grelhado",
    "dentro_dieta": True
})
print(r.status_code, r.text)

# -------------------------------
# 4️⃣ Logout
# -------------------------------
print("\n=== Logout ===")
r = s.get(f"{BASE_URL}/logout")
print(r.status_code, r.text)
