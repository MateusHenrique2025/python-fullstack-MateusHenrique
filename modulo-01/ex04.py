"""
exercicio04.py — Cadastro simples de funcionário.

Este programa cria variáveis para armazenar os dados básicos
de um funcionário (nome, idade, salário e status de atividade)
e exibe todos os valores na tela com uma única chamada a print().

Serve como exemplo introdutório de:
  - atribuição de variáveis;
  - tipos primitivos em Python (str, int, float, bool);
  - exibição de múltiplos valores com print().
"""

# Nome completo do funcionário (string de texto)
nome = "Ana Lima"

# Idade em anos completos (número inteiro)
idade = 29

# Salário mensal em reais (número decimal / float)
salario = 4500.00

# Indica se o funcionário está ativo na empresa (booleano: True ou False)
ativo = True

# Exibe todos os dados do funcionário em uma única linha, separados por espaço
print(nome, idade, salario, ativo)