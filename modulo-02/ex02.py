### 🟢 Exercício 02 – Validador de Acesso

# Leitura das credenciais
usuario = input("Usuário: ")
senha = input("Senha: ")

# Verificação em ordem: usuário primeiro, senha depois
if usuario == "admin":
    if senha == "iteam2025":
        print("✅ Acesso liberado. Bem-vindo!")
    else:
        print("❌ Senha incorreta.")
else:
    print("❌ Usuário não encontrado.")