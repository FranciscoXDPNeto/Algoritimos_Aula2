palestra = ["Ana", "Carlos", "Marina"]
workshop = ["Carlos", "João", "Ana"]
mesa_redonda = ["Marina", "João", "Paula"]

set_palestra = set(palestra)
set_workshop = set(workshop)
set_mesa = set(mesa_redonda)

todos = set_palestra & set_workshop & set_mesa

participacoes = {}
for atividade in [palestra, workshop, mesa_redonda]:
    for nome in atividade:
        participacoes[nome] = participacoes.get(nome, 0) + 1

apenas_uma = [nome for nome, qtd in participacoes.items() if qtd == 1]

todos_participantes = set_palestra | set_workshop | set_mesa

qtd_distintos = len(todos_participantes)

print("Controle de Participação no Evento")
print(f"Participaram de todas as atividades: {todos}")
print(f"Participaram de apenas uma atividade: {apenas_uma}")
print(f"Lista de participantes únicos: {todos_participantes}")
print(f"Total de participantes distintos: {qtd_distintos}")
