### 🟢 Exercício 01 – Classificador de Temperatura

# Leitura da temperatura e conversão para float
temperatura = float(input("Temperatura: "))

# Classificação conforme a tabela
if temperatura < 0:
    classificacao = "❄️ Congelante"
elif temperatura <= 14:
    classificacao = "🥶 Frio"
elif temperatura <= 24:
    classificacao = "😊 Agradável"
elif temperatura <= 34:
    classificacao = "☀️ Quente"
else:
    classificacao = "🔥 Muito quente"

# Exibição do resultado
print(f"Classificação: {classificacao}")