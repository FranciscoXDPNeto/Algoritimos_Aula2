def sistema_de_vendas():
    vendas = []  # Lista para armazenar os produtos vendidos (tupla de nome e preço)

    print("Sistema de Registro de Vendas")

    while True:
        # Solicita ao usuário o nome do produto e o preço
        nome_produto = input("Digite o nome do produto vendido (ou 'sair' para encerrar): ").strip()

        if nome_produto.lower() == 'sair':
            break

        try:
            preco_produto = float(input(f"Digite o preço do produto {nome_produto}: R$"))
        except ValueError:
            print("Preço inválido! Tente novamente.")
            continue

        vendas.append((nome_produto, preco_produto))

    # 2. Mostrar o valor total arrecadado
    total_arrecadado = sum(preco for _, preco in vendas)
    print(f"\nValor total arrecadado: R${total_arrecadado:.2f}")

    # 3. Identificar o produto mais caro e o mais barato
    if vendas:
        produto_mais_caro = max(vendas, key=lambda x: x[1])
        produto_mais_barato = min(vendas, key=lambda x: x[1])

        print(f"Produto mais caro: {produto_mais_caro[0]} - R${produto_mais_caro[1]:.2f}")
        print(f"Produto mais barato: {produto_mais_barato[0]} - R${produto_mais_barato[1]:.2f}")
    else:
        print("Nenhuma venda registrada.")

    # 4. Consultar se um produto específico foi vendido
    consulta = input("\nDigite o nome de um produto para consultar se foi vendido: ").strip()
    produtos_vendidos = [produto for produto, _ in vendas]
    
    if consulta in produtos_vendidos:
        print(f"O produto '{consulta}' foi vendido!")
    else:
        print(f"O produto '{consulta}' não foi vendido.")

# Chama a função para rodar o sistema
sistema_de_vendas()
