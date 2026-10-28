### 🟢 Exercício 04 – Contador Regressivo

# Leitura do número
n = int(input("Digite um número inteiro positivo: "))

# Contagem regressiva
while n >= 0:
    print(f"{n}...", end=" ")
    n -= 1

# Mensagem final
print("\n🚀 Lançamento!")