### 🟢 Exercício 05 – Buscador com `break`

estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

encontrado = False

for posicao, produto in enumerate(estoque):
    if produto == "Monitor":
        print(f"✅ Produto '{produto}' encontrado na posição {posicao}.")
        encontrado = True
        break

if not encontrado:
    print("Produto não encontrado no estoque.")