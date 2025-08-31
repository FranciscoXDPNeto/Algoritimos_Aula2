emprestimos = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["Senhor dos Anéis", "Paula", 8]
]

atrasados = [livro for livro in emprestimos if livro[2] > 7]

livro_mais_tempo = max(emprestimos, key=lambda item: item[2])

usuarios = {livro[1] for livro in emprestimos}

media_dias = sum(livro[2] for livro in emprestimos) / len(emprestimos)

print("Sistema de Biblioteca")
print("Livros emprestados há mais de 7 dias:")
for titulo, usuario, dias in atrasados:
    print(f"   - {titulo} ({usuario}, {dias} dias)")

print(f"Livro emprestado há mais tempo: {livro_mais_tempo[0]} ({livro_mais_tempo[2]} dias)")
print(f"3️Usuários com livros emprestados: {usuarios}")
print(f"Média de dias de empréstimo: {media_dias:.2f}")
