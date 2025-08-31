def calcular_temperaturas():
    lista_temp = []
    for i in range(7):
        temp = float(input(f'Digite a temperatura do dia {i + 1}: '))
        lista_temp.append(temp)

    media = sum(lista_temp) / len(lista_temp)

    maior = max(lista_temp)
    menor = min(lista_temp)

    acima_media = [i + 1 for i, n in enumerate(lista_temp) if n > media]

    print(f"\nA média das temperaturas é: {media:.2f}°C")
    print(f'A maior temperatura é: {maior:.2f}°C')
    print(f'A menor temperatura é: {menor:.2f}°C')
    print(f'Os dias acima da média são: {acima_media}')

calcular_temperaturas()
