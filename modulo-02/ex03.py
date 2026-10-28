### 🟢 Exercício 03 – Tabuada Interativa

# Leitura do número e conversão para inteiro
numero = int(input("Digite um número inteiro: "))

# Cabeçalho
print(f"=== Tabuada do {numero} ===")

# Laço de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:>2} = {resultado:>3}")
