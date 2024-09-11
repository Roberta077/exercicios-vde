import json

with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

valores = [item['valor'] for item in faturamento_diario if item['valor'] > 0]

media_mensal = sum(valores) / len(valores)

menor_valor = min(valores)
maior_valor = max(valores)

dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
