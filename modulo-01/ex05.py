"""
exercicio05.py — Correção de erros (debugging).

Este arquivo contém a versão corrigida do Exercício 05.
Cada erro do código original está explicado em um comentário
logo acima da linha corrigida, indicando:
  - o tipo de erro;
  - a mensagem que o Python exibia;
  - a correção aplicada.

Objetivo: praticar leitura de mensagens de erro e debugging básico.
"""

# ERRO 1 — Uso indevido de maiúscula em função built-in.
# Original: Print("...")
# O Python é case-sensitive. A função correta é "print" (minúscula).
# Erro original: NameError: name 'Print' is not defined
print("Bem-vindo ao curso de Python")

# ERRO 2 — String não fechada (faltou aspas duplas no final).
# Original: nome = "Carlos
# Erro original: SyntaxError: unterminated string literal
nome = "Carlos"

# Esta linha já estava correta no original.
# Concatenação de string literal com a variável "nome".
print("Aluno: " + nome)

# ERRO 3 — Texto sem aspas sendo tratado como nome de variável.
# Original: print(Curso de Python)
# Sem aspas, "Curso", "de" e "Python" viram nomes de variáveis inexistentes.
# Erro original: SyntaxError: invalid syntax
print("Curso de Python")