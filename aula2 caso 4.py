vendas = [10, 15, 20, 5, 0, 8, 12, 14, 18, 25,
          12, 8, 7, 10, 20, 16, 15, 18, 20, 10,
          9, 2, 5, 12, 14, 18, 22, 25, 13, 18, 12]

total_vendas = sum(vendas)

maior_venda = max(vendas)
menor_venda = min(vendas)

dia_maior = vendas.index(maior_venda) + 1  
dia_menor = vendas.index(menor_venda) + 1

media_vendas = total_vendas / len(vendas)

dias_acima_media = [i+1 for i, v in enumerate(vendas) if v > media_vendas]

print("Análise de Vendas Mensais")
print(f"Total de vendas no mês: {total_vendas}")
print(f"Dia com mais vendas: Dia {dia_maior} ({maior_venda} vendas)")
print(f"Dia com menos vendas: Dia {dia_menor} ({menor_venda} vendas)")
print(f"Média de vendas por dia: {media_vendas:.2f}")
print(f"Dias com vendas acima da média: {dias_acima_media}")
