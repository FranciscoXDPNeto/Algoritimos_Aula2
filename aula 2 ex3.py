def lista_de_compras():    
    lista_compras = []

    print('''Digite os itens que deseja adicionar a lista de compras. 
(Digite 'sair' para encerrar a lista)''')

    while True:
        entrada = input("Digite o item: ")
      
        if entrada.lower() == 'sair':   
            break
        
        if entrada.strip():  
            lista_compras.append(entrada)
        else:
            print("Por favor, insira um item válido.")

    lista_compras.sort()

    print("Lista de compras final (em ordem alfabética):")
    for item in enumerate(lista_compras, 1):
        print(f"*{item}")

lista_de_compras()