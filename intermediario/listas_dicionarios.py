# intermediario/listas_dicionarios.py
# Manipulação de listas e dicionários

# Lista de dicionários
alunos = [
    {"nome": "Maria", "nota": 8.5},
    {"nome": "Pedro", "nota": 7.0},
    {"nome": "Ana", "nota": 9.2},
]

# Filtrar alunos aprovados
aprovados = [a["nome"] for a in alunos if a["nota"] >= 7.0]
print("Aprovados:", aprovados)

# Atualizar nota de um aluno
for aluno in alunos:
    if aluno["nome"] == "Pedro":
        aluno["nota"] = 8.0

print("Alunos:", alunos)
