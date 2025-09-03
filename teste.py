import requests

BASE_URL = "http://127.0.0.1:5000"

# -------- Criar usuário --------
print("\n--- Criando usuário ---")
r = requests.post(f"{BASE_URL}/create_user", json={
    "nome": "edison",
    "senha": "1234"
})
print("Status:", r.status_code)
print("Resposta:", r.text)


# -------------------------------
# 7️⃣ Criar refeição
# -------------------------------
r = requests.post(f"{BASE_URL}/create_refeicao", json={
    "nome_refeicao": "Almoço",
    "descricao": "Arroz, feijão e frango grelhado",
    "dentro_dieta": True,
    "user_id": 1
})
print("Status:", r.status_code)
print("Resposta:", r.text)
