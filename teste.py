import requests

BASE_URL = "http://127.0.0.1:5000"

print("\n=== Criar Usuário ===")
r = requests.post(f"{BASE_URL}/create_user", json={"nome": "edison", "senha": "123"})
print(r.status_code, r.text)

print("\n=== Login ===")
s = requests.Session()  # mantém cookies de sessão
r = s.post(f"{BASE_URL}/login", json={"nome": "edison", "senha": "123"})
print(r.status_code, r.text)


print("\n=== Criar Refeição ===")
r = s.post(f"{BASE_URL}/create_refeicao", json={
    "nome_refeicao": "Almoço",
    "descricao": "Arroz, feijão e frango",
    "dentro_dieta": True
})
print(r.status_code, r.text)

# suponha que a refeição criada tenha id = 1
print("\n=== Editar Refeição ===")
r = s.put(f"{BASE_URL}/editar-refeicao/1", json={
    "nome_refeicao": "Almoço Atualizado",
    "descricao": "Arroz integral, feijão e peito de frango",
    "dentro_dieta": False
})
print(r.status_code, r.text)

print("\n=== Logout ===")
r = s.get(f"{BASE_URL}/logout")
print(r.status_code, r.text)
