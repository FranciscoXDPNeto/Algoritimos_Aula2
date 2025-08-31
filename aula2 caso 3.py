# [nome, quantidade, preco_unitario]
estoque = [
    ["Arroz", 10, 18.00],
    ["Feijão", 3, 10.50],
    ["Macarrão", 15, 8.50],
    ["Óleo", 2, 8.50],
    ["Açúcar", 7, 6.50],
]

valor_total = sum(qtd * preco for _, qtd, preco in estoque)

produto_maior_valor = max(estoque, key=lambda item: item[1] * item[2])

estoque_baixo = [nome for nome, qtd, _ in estoque if qtd < 5]

def buscar_produto(nome_busca):
    for nome, qtd, preco in estoque:
        if nome.lower() == nome_busca.lower():
            return f"Produto: {nome} | Quantidade: {qtd} | Preço: R${preco:.2f}"
    return "Produto não encontrado!"

print("Controle de Estoque")
print(f"Valor total em estoque: R${valor_total:.2f}")
print(f"Produto de maior valor: {produto_maior_valor[0]} (R${produto_maior_valor[1]*produto_maior_valor[2]:.2f})")
print(f"Produtos com estoque < 5: {estoque_baixo}")

nome_procurado = input("Digite o nome do produto que deseja buscar: ")
print(buscar_produto(nome_procurado))

