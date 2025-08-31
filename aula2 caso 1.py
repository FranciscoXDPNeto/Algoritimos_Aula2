presencas = {
    "Segunda": {"Francisco", "Brunna", "Fernando", "Angela"},
    "Terça":   {"Francisco", "Fernando", "Angela"},
    "Quarta":  {"Francisco", "Brunna", "Fernando", "Angela"},
    "Quinta":  {"Francisco", "Fernando"},
    "Sexta":   {"Francisco", "Brunna", "Fernando", "Angela"},
}

presentes_todos = set.intersection(*presencas.values())

presentes_algum = set.union(*presencas.values())
faltaram_algun_dia = presentes_algum - presentes_todos

contagem_presencas = {}
for dia, alunos in presencas.items():
    for aluno in alunos:
        contagem_presencas[aluno] = contagem_presencas.get(aluno, 0) + 1

print("Presentes todos os dias:", presentes_todos)
print("Faltaram em pelo menos um dia:", faltaram_algun_dia)
print("Total de presenças por aluno:", contagem_presencas)
